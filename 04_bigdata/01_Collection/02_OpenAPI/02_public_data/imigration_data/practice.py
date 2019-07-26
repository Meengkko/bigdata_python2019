import urllib.request
import datetime
import json
from operator import itemgetter
# service = 출입국 응용 프로그램
access_key = ["Key_1","Key_2","Key_3","Key_4"]

# class TrafficExceeded(Exception):
#     pass


def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


# [CODE 1]
def getNatVisitor(yyyymm, nat_cd, ed_cd, key_index):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey="+access_key[key_index]
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = end_point + parameters
    retData = get_request_url(url)

    if retData == None:
        return None
    else:
        if eval(retData)['response']['header']['resultMsg'] == "LIMITED NUMBER OF SERVICE REQUESTS EXCEEDS ERROR.":
            return {}
        # print(retData)
        return json.loads(retData)


def main():
    jsonResult = []

    national_code = {"중국": "112"}
    ed_cd = "E"

    nStartYear = 2016
    nStartMonth = 1
    nEndYear = 2017
    nEndMonth = 12

    with open("national_code_selected.txt", 'r', encoding='utf-8') as nat_file:
        national_lines = nat_file.readlines()

    for national_line in national_lines:
        national_list = national_line.strip().split('=')
        national_list[1] = national_list[1].replace(' ','')
        if '중국' in national_list:
            continue
        national_code[national_list[1]] = national_list[0]

    # print(national_code)
    key_index = 0
    for nation in list(national_code.keys()):
        total_visit = 0
        for year in range(nStartYear, nEndYear + 1):
            for month in range(nStartMonth, nEndMonth + 1):
                yyyymm = "{0}{1:0>2}".format(str(year), str(month))
                jsonData = getNatVisitor(yyyymm, national_code[nation], ed_cd, key_index)
                if not jsonData:
                    print("가용한 트래픽을 모두 사용하였습니다. 키값을 변경합니다.")
                    key_index = key_index + 1
                    try:
                        jsonData = getNatVisitor(yyyymm, national_code[nation], ed_cd, key_index)
                    except IndexError as e:
                        print(e)
                        print("키 값이 모두 소진되었습니다 프로그램을 종료합니다.")
                        return
                try:
                    if jsonData['response']['header']['resultMsg'] == 'OK':
                        iTotalVisit = jsonData['response']['body']['items']['item']['num']
                        total_visit += iTotalVisit
                except KeyError:
                    pass

        jsonResult.append([nation, total_visit])

    jsonResult.sort(key=itemgetter(1), reverse=True)

    with open('해외방문객정보[%d개국](%d%d ~ %d%d).json' % (len(national_code), nStartYear, nStartMonth, nEndYear, nEndMonth), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)


if __name__ == '__main__':
    main()

