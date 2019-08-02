import urllib.request
import datetime
import json
import time
import threading
import ctypes

json_weather_result = []
access_key = 'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
x_coodinate = "89"
y_coodinate = "91"

dust_access_key = 'arUGyHfSIvuuisVWulspIDqDRNaEEkPTXBKzLni5OzcFJoxrCbEaywqixKDH%2F3wmqB8wEFFKci7512Q7q%2BwyiA%3D%3D'
city_name = '대구'

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
scheduler_cycle = 3600
yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))

def get_Requrest_URL(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def get_dust_URL():
    # p18
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    parameters = "?sidoName=%s&pageNo=1&numOfRows=10&ServiceKey=%s&ver=1.3&_returnType=json" \
                 % (urllib.parse.quote(city_name), dust_access_key)
    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_dust_Json():
    jsonData = get_dust_URL()
    for data in jsonData['list']:
        if data["stationName"] == '신암동':
            json_dust_result = data

    with open('대구_신암동_실시간_미세먼지_%s.json' % (yyyymmdd), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_dust_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    # print('대구_실시간_미세먼지_%s.json' % (yyyymmdd))
    return json_dust_result

def get_Weather_URL(day_time):
    base_date = time.strftime('%Y%m%d', time.localtime(time.time()))
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = ("?base_date=%s&base_time=%s&nx=%s&ny=%s&_type=json&numOfRows=100&serviceKey=%s") \
                 %(base_date,day_time,x_coodinate,y_coodinate,access_key)

    url = end_point + parameters
    retData = get_Requrest_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    jsonData = get_Weather_URL(day_time)

    for data in jsonData['response']['body']['items']['item']:
        json_weather_result.append(data)

    with open('동구_신암동_초단기예보조회_%s.json' % (yyyymmdd), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    # print('동구_신암동_초단기예보조회_%s.json' % (yyyymmdd))
    return json_weather_result

def get_Realtime_Weather_Info():
    if time.localtime().tm_min in range(0,31):
        real_time = str(time.localtime().tm_hour - 1) + '59'
    else:
        real_time = time.strftime('%H%M', time.localtime(time.time()))
    if len(real_time) == 3:
        real_time = '0' + real_time
    return Make_Weather_Json(real_time)

def terminate_ai_mode():
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def update_scheduler():
    while True:
        time.sleep(scheduler_cycle)
        print(f"스케줄러 작동..  {scheduler_cycle}초 주기")
        dust_data = Make_dust_Json()
        weather_data = get_Realtime_Weather_Info()
        AI_Mode(dust_data, weather_data)

def AI_Mode(dust_data, weather_data):
    global g_Balcony_Windows
    global g_Radiator
    w_value = t_value = ''
    for data in weather_data:
        if not w_value and "RN1" in data["category"]:
            w_value = data["fcstValue"]
        if "T1H" in data['category'] and not t_value:
            t_value = data["fcstValue"]
    if int(dust_data['pm10Value']) > 10 or int(dust_data['pm25Value']) > 30:
        if g_Balcony_Windows:
            g_Balcony_Windows = not g_Balcony_Windows
            print('\n미세먼지가 높아 발코니 창문이 닫힙니다')
    if 0 < w_value and g_Balcony_Windows:
        g_Balcony_Windows = not g_Balcony_Windows
        print('\n비나 눈이 올 가능성이 높아 발코니 창문이 닫힙니다')
    if 28 < t_value and not g_Radiator:
        g_Radiator = True
        g_Balcony_Windows = False
        print("실외온도 28도 이상입니다. 창문을 닫고 에어컨을 킵니다.")

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: " %device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print('')
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동 완료!")
        else:
            print("중지!")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("중지 완료!")
    elif menu_num == 3:
        get_Realtime_Weather_Info()
        Make_dust_Json()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 손병찬 -")
ai_scheduler = threading.Thread(target=update_scheduler)
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif (menu_num == 4):
        pass
    elif(menu_num == 5):
        break