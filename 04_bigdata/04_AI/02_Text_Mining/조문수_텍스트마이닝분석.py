import urllib.request
from bs4 import BeautifulSoup
import codecs
from konlpy.tag import Okt

#- 과제 수행 목표: 한글 text를 대상으로 한 텍스트마이닝 적용
#- 데이터 출처 및 해석: 사용자에게 검색어를 입력받아 네이버 기사제목을(1~30페이지까지) 웹크롤링 하여 많이 사용된 명사 출력
#- 텍스트 데이터 의미: 사용자 검색어의 네이버 기사 제목
#- 예측 항목: 많이 사용된 명사 출력
#- 어휘 분류 기준: 단어 출현 횟수 (어미, 조사, 마침표 제거)
#- 유의어 (유의어가 없을 경우 결과에 가장 많은 영향을 미친 단어 표시): 검색어에따라 다름

def Search2(Search):
    title_text = []
    start = 1
    location = urllib.parse.quote(Search)
    f = open(f"{Search}기사제목.txt", 'w', encoding="utf8")
    f.close()
    f = open(f"{Search}기사제목.txt", 'a', encoding="utf8")
    for i in range(1, 31):
        html = urllib.request.urlopen('https://search.naver.com/search.naver?&where=news&query=' + location + '&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=108&start=' + str(start) + '&refresh_start=0')
        soup = BeautifulSoup(html, 'html.parser')
        up_down = soup.findAll('a', attrs={'class': '_sp_each_title'})
        for i in range(len(up_down)):
            title_text.append(up_down[i]['title'])
            print(up_down[i]['title'])
            f.write(f'{up_down[i]["title"]}\n')
        start += 10
    f.close()

    fp = codecs.open(f"{Search}기사제목.txt", "r", encoding="utf-8")
    # fp = codecs.open("문재인_국정연설문_2017.txt", "r", encoding="utf-8")
    text = fp.read()
    # 텍스트를 한 줄씩 처리하기 ---(2)
    # twitter = Twitter()
    okt = Okt()
    word_dic = {}
    lines = text.split("\r\n")
    for line in lines:
        malist = okt.pos(line, norm=True, stem=True)
        for word in malist:
            if word[1] == "Noun":  # 명사 확인하기 ---(3) # 주로 명사에 뜻이 담겨져 있다고 판단해서
                if not (word[0] in word_dic):
                    word_dic[word[0]] = 0
                word_dic[word[0]] += 1  # 카운트하기
    # 많이 사용된 명사 출력하기 ---(4)
    keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
    print('\n주요 어휘 분석')
    for word, count in keys[:50]:
        if count > 1:
            print("{0} ({1})".format(word, count))


while 1:
    print('-------- 네이버 기사 검색,저장(1~30페이지까지의 기사제목 명사 추출) --------')
    Search = input('검색어 입력(종료키:0): ')
    if Search == '0':
        exit()
    else:
        Search2(Search)





