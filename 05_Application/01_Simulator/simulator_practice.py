import threading
import time
import ctypes
import urllib.request
import urllib.parse
import json
import datetime
import xml.etree.ElementTree as ET


g_Radiator = False
g_Air_conditioner = False
g_Balcony_Windows = True
g_Air_cleaner = False
g_AI_Mode = False
# Updated each 30minutes
schedule_cycle = 1800
access_key_rain = "key1"  # 공공데이터 포털 : 동네예보정보조회서비스
access_key_dust = "key2"  # 공공데이터 포털 : 대기오염정보 조회 서비스 -> 시도별 실시간 측정정보 조회
open_and_close = {True: "열림", False: "닫힘"}
air_level = {1: "좋음", 2: "보통", 3: "나쁨", 4: "매우 나쁨"}


def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


def get_Weather_URL(base_date, base_time, nx="89", ny="91", numOfRows = "30"):
    # 공공데이터 포털 : 동네예보정보조회서비스
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key_rain
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
        # print(retData)
        return json.loads(retData)


def get_dust_url():
    # 공공데이터 포털 : 대기오염정보 조회 서비스 -> 시도별 실시간 측정정보 조회
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?serviceKey=" + access_key_dust
    parameters += "&pageNo=1"
    parameters += "&sidoName=" + urllib.parse.quote("대구")
    parameters += "&numOfRows=20"
    parameters += "&ver=1.3"

    url = end_point + parameters
    retData = get_request_url(url)

    if retData == None:
        return None
    else:
        return retData


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


def terminate_ai_mode():
    ''' Terminate a python thread from another thread.
    : param thread: a threading.Thread instance '''

    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident), exc)

    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        '''if it returns a number greater than one, you're in trouble,
        and you should call it again with exc=NULL to revert the effect'''
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThread_SetAsyncExc failed")


def update_scheduler():
    global g_Balcony_Windows
    while True:
        time.sleep(schedule_cycle)
        try:
            weather_json = make_weather_json()
            print("\n\n신암동 실시간 강수 및 미세먼지 예보")
            print("=================================")
            print("대기질 & 미세먼지 >>")
            dust_xml = get_dust_url() # 대기정보는 xml로 받습니다.
            root_node = ET.fromstring(dust_xml)
            for station in root_node.find('body').find('items').getiterator('item'):
                if station.findtext("stationName") == '신암동':
                    print("\t날짜 및 시간: %s" % station.findtext('dataTime'))
                    print("\t아황산가스 농도: %sppm" % station.findtext('so2Value'))
                    print("\t이산화질소 농도: %sppm" % station.findtext('no2Value'))
                    print("\t미세먼지(PM10) 1시간 등급자료: %s" % air_level[int(station.findtext('pm10Grade1h'))])
                    print("\t미세먼지(PM25) 1시간 등급자료: %s" % air_level[int(station.findtext('pm25Grade1h'))])
                    if int(station.findtext('pm10Grade1h')) >= 3 or int(station.findtext('pm25Grade1h')) >= 3:
                        print("미세먼지 수치가 기준치 이상이므로 자동으로 창문을 닫습니다.")
                        g_Balcony_Windows = False
            print("\n강수정보 >>")
            for forecast in weather_json:
                if forecast["category"] == "RN1":
                    print("\t강수 지수 예보(%s시 %s분): %d"
                          % (str(forecast["fcstTime"])[:2], str(forecast["fcstTime"])[2:], forecast["fcstValue"]))
                    if abs(int(forecast["fcstTime"]) - int(time.strftime("%H%M"))) < 100 and int(forecast["fcstValue"]) > 10:
                        print("강수가 예상되므로 자동으로 창문을 닫습니다.")
                        g_Balcony_Windows = False

        except IndexError:
            print("정보를 불러오지 못합니다.")


def total_status():
    print("\n장비상태를 확인합니다.\n===================")
    print("1. 난방기: %s" % open_and_close[g_Radiator])
    print("2. 에어컨: %s" % open_and_close[g_Air_conditioner])
    print("3. 발코니 창문: %s" % open_and_close[g_Balcony_Windows])
    print("4. 공기청정기: %s" % open_and_close[g_Air_cleaner])


def manipulator():
    global g_Radiator, g_Air_conditioner, g_Balcony_Windows, g_Air_cleaner
    while True:
        print("홈 서비스 수동 조작")
        total_status()
        print("5. 상위 메뉴")
        mani_option = input("어떤 기기의 상태를 변경하시겠습니까?")
        if mani_option == '1':
            g_Radiator = not g_Radiator
        elif mani_option == '2':
            g_Air_conditioner = not g_Air_conditioner
        elif mani_option == '3':
            g_Balcony_Windows = not g_Balcony_Windows
        elif mani_option == '4':
            g_Air_cleaner = not g_Air_cleaner
        elif mani_option == '5':
            print("수동 조작을 중지합니다.")
            return
        else:
            print("잘못된 명령입니다.")


def operating_my_json(sim_json):
    is_dustmode = False
    is_rainshowermode = False
    global g_Radiator, g_Air_conditioner, g_Balcony_Windows, g_Air_cleaner
    rain_shower = {0: "없음", 1: "있음"}
    for simulation in sim_json['response']['body']['items']['item']:
        time.sleep(2)
        print("\t날짜 및 시간: %s" % simulation['datetime'])
        print("\t아황산가스 농도: %dppm" % simulation['so2Value'])
        print("\t이산화질소 농도: %dppm" % simulation['no2Value'])
        print("\t미세먼지(PM10) 1시간 등급자료: %s" % air_level[simulation['pm10Grade1h']])
        print("\t미세먼지(PM25) 1시간 등급자료: %s" % air_level[simulation['pm25Grade1h']])
        print("\t강우확률: %d%%" % simulation['RP'])
        print("\t소나기 유무: %s" % rain_shower[simulation['RS']])
        if (simulation['pm10Grade1h'] > 2 or simulation['pm25Grade1h'] > 2) and not is_dustmode:
            g_Balcony_Windows = False
            g_Air_cleaner = True
            is_dustmode = True
            print("\n(경고!) 미세먼지 수치가 높습니다. 창문을 닫고 공기청정기를 작동시킵니다.")


        if (simulation['RP'] > 50 or simulation['RP'] == 1) and not is_rainshowermode:
            g_Balcony_Windows = False
            g_Air_conditioner = True
            is_rainshowermode = True
            print("\n(경고!) 소나기가 오거나 강우확률이 높습니다 창문을 닫고 에어컨을 작동시킵니다.")

        if simulation['pm10Grade1h'] <= 2 and simulation['pm25Grade1h'] <= 2 and simulation['RP'] < 30 and simulation['RP'] == 0:
            is_dustmode = False
            is_rainshowermode = False
            if g_Air_conditioner or g_Air_cleaner:
                g_Air_cleaner = False
                g_Air_conditioner = False
            if not g_Balcony_Windows:
                window_open = input("날씨가 쾌적합니다. 창문을 여시겠습니까? (y/n)")
                if window_open == 'y':
                    g_Balcony_Windows = True

        show_option = input("가전현황을 보시겠습니까? (y/n) ")
        if show_option == 'y':
            total_status()


def simulator():
    print("시뮬레이션 ver1.0")
    time.sleep(1)
    menu_option = input("1. 맑은날 데모\n2. 흐린날 데모\n메뉴 선택: ")
    if menu_option == '1':
        with open("ex_sunny.json", 'r') as sun_file:
            sunny_json = json.loads(sun_file.read())
            operating_my_json(sunny_json)
    elif menu_option == '2':
        with open("ex_rainy.json", 'r') as rain_file:
            rainy_json = json.loads(rain_file.read())
            operating_my_json(rainy_json)
    else:
        print("잘못된 입력입니다.")

    print("시뮬레이션 종료\n")


while True:
    menu_num = input("1. 장비상태 확인\n2. 장비 제어\n3. 스마트모드\n4. 시뮬레이션 모드\n5. 프로그램 종료\n메뉴 입력: ")
    if menu_num == '1':
        total_status()
    elif menu_num == '2':
        manipulator()
    elif menu_num == '3':
        print("스마트 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode:
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass

            print("정지 완료!")
    elif menu_num == '4':
        simulator()
    elif menu_num == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다.")