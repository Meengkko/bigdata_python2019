import json
import operator


def main():
    key_word = input("도메인 데이터 분석 키워드: ")
    try:
        with open("%s_naver_news.json" % key_word, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print("해당되는 파일명이 없습니다.")
        return

    url_list = {}
    url_missed = 0
    domain_number = 0
    case_number = 0
    print("\n데이터 분석을 시작합니다..\n")
    for data in json_data:
        try:
            url_extracted = data["org_link"].split('/')[2]
            case_number = case_number + 1
            if url_extracted in list(url_list.keys()):
                url_list[url_extracted] = url_list[url_extracted] + 1
            else:
                domain_number = domain_number + 1
                url_list[url_extracted] = 1
        except IndexError:
            url_missed = url_missed + 1
            print("\'org_link\'가 없는 기사를 발견했습니다.")

    url_list_sorted = sorted(url_list.items(), key=operator.itemgetter(1), reverse=True)

    print("\n<네이버 검색 빅데이터 분석>")
    print("검색어: %s\n전체 도메인 수: %d\n전체 건수: %d\n부정확한 데이터수: %d" % (key_word, domain_number, case_number, url_missed))
    print("\n- 도메인 별 뉴스 기사 분석")

    [print(">>", domain, ":", value, "건") for domain, value in url_list_sorted]


main()
