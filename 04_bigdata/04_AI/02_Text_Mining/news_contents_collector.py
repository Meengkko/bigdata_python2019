'''
이 프로그램은 포털 메인에 뜬 네이버, 다음 뉴스의 '본문'을 끌어와
해당 카테고리 별로 연관어 분석을 하는 프로그램입니다.
'''

import re
import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec


def get_article_naver(section):
    url_section = {'정치': '100', '경제': '101', '사회': '102', '문화': '103', '세계': '104', 'IT': '105'}
    url_with_option = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=' + url_section[section]
    html = urllib.request.urlopen(url_with_option)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('div')

    domain_list = []

    for tag in tags:
        if 'class' not in tag.attrs.keys():
            continue
        if 'cluster_text' not in tag.attrs['class']:
            continue
        domain_list.append(str(tag.a['href']))

    article_text = []

    for domain in domain_list:
        html = urllib.request.urlopen(domain)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('div')
        for tag in tags:
            text_article_raw = ''
            if 'id' not in tag.attrs.keys():
                continue
            if tag.attrs['id'] == 'articleBodyContents':
                text_article_raw = tag.text.strip()
            text_article = re.sub('//.+추가|fun.+{}', '', text_article_raw)
            if text_article != '':
                article_text.append(text_article)
    return article_text


def get_article_daum(section):
    daum_url_cat = {'정치': 'politics/', '경제': 'economic/', '사회': 'society/',
                    '문화': 'culture/', '세계': 'foreign/', 'IT': 'digital/'}
    daum_url = 'https://media.daum.net/' + daum_url_cat[section]
    html = urllib.request.urlopen(daum_url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')

    domain_list_daum = []

    for tag in tags:
        if 'class' not in tag.attrs.keys():
            continue
        class_name_joined = ''.join(tag.attrs['class'])
        if re.search(r'#article', class_name_joined):
            domain_candid = tag.attrs['href']
            if domain_candid not in domain_list_daum:
                domain_list_daum.append(tag.attrs['href'])

    article_text = []

    for domain_daum in domain_list_daum:
        html = urllib.request.urlopen(domain_daum)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('p')
        text_checker = ['dmcf-pid', 'dmcf-ptype']

        for tag in tags:
            if list(tag.attrs.keys()) == text_checker:
                article_text.append(tag.text)
    return article_text


show_option = '''
원하는 뉴스 갈래를 입력하세요.
===========================
1. 정치   2. 경제   3. 사회
4. 문화   5. 세계   6. IT
===========================
>>> '''
option_selected = input(show_option)
keyword_input = input("어떤 단어와 연관성 검색을 하시겠습니까? ")
news_cat = {'1': '정치', '2': '경제', '3': '사회', '4': '문화', '5': '세계', '6': 'IT'}
total_article = get_article_naver(news_cat[option_selected])
total_article += get_article_daum(news_cat[option_selected])

okt = Okt()
results = []
for line in total_article:
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미 / 조사 / 구두점 등은 대상에서 제외
        if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign", "Number", "Suffix", "Verb"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)

wakati_file = 'news.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('news.model')
print("\n\n================ 분석완료 ================")

similar_words = model.most_similar(positive=[keyword_input])
for word_set in similar_words:
    print(f'{word_set[0]:<10}: {word_set[1]}')
