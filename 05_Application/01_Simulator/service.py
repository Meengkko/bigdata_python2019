import urllib.request
import datetime
import json
import math
# service = 관광자원통계서비스
access_key = "4mfMHAeDyEtKHldadmZhsowh7OOwr70mw2uEgJrbaQHfuxNTLZdsDJGOVpngk64lN9oVQmBlgh%2BzSTaIKq8TxA%3D%3D"

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
def getTourPointVisitor():
    end_point = "http://data.insight.go.kr:8080/openapi/service/PriceInfo"

    parameters = "?serviceKey="+access_key
    parameters += "&itemCode" + "A019170"
    parameters += "&startDate=" + "20150710"
    parameters += "&endDate=" + "20190711"


    url = end_point + parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)


# def getTourPointData(item, yyyymm, jsonResult):
#     addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
#     gungu = '' if 'gungu' not in item.keys() else item['gungu']
#     sido = '' if 'sido' not in item.keys() else item['sido']
#     resNm = '' if 'resNm' not in item.keys() else item['resNm']
#     rnum = 0 if 'rnum' not in item.keys() else item['rnum']
#     ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
#     NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
#
#     jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd, 'gungu': gungu, 'sido': sido
#                           , 'resNm': resNm, 'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})
#
#     return

def main():
    print(getTourPointVisitor())


if __name__ == '__main__':
    main()

