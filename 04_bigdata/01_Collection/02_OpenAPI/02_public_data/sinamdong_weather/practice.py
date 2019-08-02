import urllib.request
import datetime
import json
import time

access_key = "ex8oX05eJbnq7u6lRslrlDFQpKAvAjXg%2BxyHiaXGj9sXSbGNE02qhb2TVsh3cryHNLmlHaJgBtdTMqjqg0HUeQ%3D%3D"


def get_request_url(url):
    url = url.encode('utf-8')
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
def get_Weather_URL(base_date, base_time, nx="89", ny="91", numOfRows = "30"):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey="+access_key
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&numOfRows=" + numOfRows

    url = end_point + parameters
    retData = get_request_url(url)

    if retData == None:
        return None
    else:
        if eval(retData)['response']['header']['resultMsg'] == "LIMITED NUMBER OF SERVICE REQUESTS EXCEEDS ERROR.":
            return {}
        print(retData)
        return json.loads(retData)


def make_weather_json():

    base_time = time.strftime("%H%M")
    if int(time.strftime("%M")) < 30:
        base_time = str(int(time.strftime("%H")) - 1) + "59"

    json_data = []

    raw_data = get_Weather_URL(time.strftime("%Y%m%d"), base_time)
    data_list = raw_data['response']['body']['items']['item']
    for weather_dict in data_list:
        json_data.append(weather_dict)

    return json_data


def main():

    jsonResult = make_weather_json()

    with open('동구_신암동_초단기예보조회_%s%s.json' % (time.strftime("%Y%m%d"), time.strftime("%H%M")), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)


if __name__ == '__main__':
    main()

