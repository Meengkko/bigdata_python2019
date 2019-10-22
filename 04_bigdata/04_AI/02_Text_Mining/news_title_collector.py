import re
import urllib.request
from bs4 import BeautifulSoup
import csv


def make_title_dict_naver():
    naver_cat = {'100': '정치', '101': '경제', '102': '사회', '103': '문화', '104': '세계', '105': 'IT'}

    html = urllib.request.urlopen('https://news.naver.com/')
    soup = BeautifulSoup(html, 'html.parser')

    main_news_expression = r'sid1=([0-9]{3})&oid'
    ranking_news_expression = r'rankingSectionId=([0-9]{3})'

    tags = soup.find_all('a')

    dict_naver_a = title_classifier_naver(tags, naver_cat, main_news_expression)
    dict_naver_b = title_classifier_naver(tags, naver_cat, ranking_news_expression)

    dict_naver = merge_news_dict(dict_naver_a, dict_naver_b)

    return dict_naver


def title_classifier_naver(bs_tags, index_dict, re_expression):
    cat_dict = {'정치': [], '경제': [], '사회': [], '문화': [], '세계': [], 'IT': []}
    index_list = list(index_dict.keys())
    pattern_obj = re.compile(re_expression)
    for tag in bs_tags:
        match_obj = pattern_obj.search(str(tag['href']))
        news_index = ''
        if match_obj:
            news_index = match_obj.group(1)

        if news_index in index_list:
            news_cat = index_dict[news_index]
            news_title = str(tag.text).strip()
            if news_title:
                cat_dict[news_cat].append(news_title)
    return cat_dict


def make_title_dict_daum():
    domain_list = ['정치', '경제', '사회', '문화', '세계', 'IT']
    title_dictionary_daum = {}
    for new_cat in domain_list:
        title_dictionary_daum[new_cat] = get_titles_daum(new_cat)

    return title_dictionary_daum


def get_titles_daum(domain):
    daum_cat = {'정치': 'politics/', '경제': 'economic/', '사회': 'society/',
                '문화': 'culture/', '세계': 'foreign/', 'IT': 'digital/'}
    url_html = 'https://media.daum.net/'
    url_html += daum_cat[domain]

    html = urllib.request.urlopen(url_html)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('a')

    title_list = []
    for tag in tags:
        attribute_dict = tag.attrs
        if 'class' not in attribute_dict.keys():
            continue
        if attribute_dict['class'][0] != 'link_txt':
            continue
        if len(attribute_dict['class']) < 2:
            continue
        if re.search(r'article', tag.attrs['class'][1]):
            title_list.append(str(tag.text))

    return title_list


def merge_news_dict(dict_a, dict_b):
    regular_keys = ['정치', '경제', '사회', '문화', '세계', 'IT']
    dict_result = {}
    for keya in regular_keys:
        dict_result[keya] = dict_a[keya] + dict_b[keya]
    return dict_result


data_prototype = merge_news_dict(make_title_dict_naver(), make_title_dict_daum())

file_format = [["real_time_news_title.csv", "w"], ["accumulative_news_cat.csv", "a"]]

input_option = '''저장할 파일 포멧을 선택하세요.
1. 실시간 뉴스 제목
2. 현재 뉴스 제목 누적하여 저장
=============================
>>> '''

input_format = int(input(input_option)) - 1

with open(file_format[input_format][0], file_format[input_format][1], newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for key, value_list in data_prototype.items():
        for value in value_list:
            value = value.strip()
            writer.writerow([key, value])
        writer.writerow([])
