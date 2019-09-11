import urllib.request
import datetime
import json
import csv

# 서비스명: 실시간 수도정보 수질(시간) 조회 서비스

access_key = "sfPkIXPkje00cL1WP0GNzD%2BNDv015JrEjaAE0p3KEKTONcNwW%2F5D4IGVDxedGAbIbtzVkPQlQfCEXLiK0m31EA%3D%3D"
output_file = '2018년_1월_취수장별_수질정보.csv'
start_date_setting = '2019-01-01'
start_timer = '11'
end_date_setting = '2019-01-01'
end_timer = '12'


csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['정수장','지역','PH수치','Ph단위','탁도수치','탁도단위','잔여염소', '염소단위']
filewriter.writerow(header_list)


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
def get_water_data(start_date, end_date, start_time, end_time, page_number):

    end_point = "http://apis.data.go.kr/B500001/rwis/waterQuality/list"

    parameters = "?serviceKey=" + access_key
    parameters += "&_type=json"
    parameters += "&stDt=" + start_date
    parameters += "&stTm=" + start_time
    parameters += "&edDt=" + end_date
    parameters += "&edTm=" + end_time
    parameters += "&liIndDiv=1"
    parameters += "&numOfRows=10"
    parameters += "&pageNo=" + str(page_number)

    url = end_point + parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        print(url)
        return json.loads(retData)


#[CODE 2]
def get_water_json_data(item):
    filtration = 'Nah' if 'fcltyMngNm' not in item.keys() else item['fcltyMngNm']
    region = 'Nah' if 'fcltyAddr' not in item.keys() else item['fcltyAddr']
    phVal = 0.0 if 'phVal' not in item.keys() else item['phVal']
    phUnit = 'Nah' if 'phUnit' not in item.keys() else item['phUnit']
    turbidity = 0.0 if 'tbVal' not in item.keys() else item['tbVal']
    turbidUnit = 'Nah' if 'tbUnit' not in item.keys() else item['tbUnit']
    chlorine = 0.0 if 'clVal' not in item.keys() else item['clVal']
    chlorineUnit = 'Nah' if 'clUnit' not in item.keys() else item['clUnit']

    row_list = [filtration, region, float(phVal), phUnit, float(turbidity), turbidUnit, float(chlorine), chlorineUnit]
    filewriter.writerow(row_list)

    return


def main():
    nPagenum = 1

    while True:
        json_data = get_water_data(start_date_setting, end_date_setting, start_timer, end_timer, nPagenum)

        if json_data['response']['header']['resultCode'] == '00':

            if json_data['response']['body']['items'] == '':
                return
            else:
                for item in json_data['response']['body']['items']['item']:
                    get_water_json_data(item)
        nPagenum += 1


if __name__ == '__main__':
    main()
    csv_out_file.close()
