from socket import *
from random import randint
import urllib.request
import datetime
import json
import time
import threading
import ctypes
from bs4 import BeautifulSoup
import re


access_key = "YJnH%2FzEygxtOA3TfMABTPh%2FZ4Ig8dbEI%2FJ%2B2wvfh%2B%2FG4BoUzdVieV0YMyKRc7MEMcE9OcxfXZJ5gUouMZ2Sw6g%3D%3D"


def terminate_ai_mode():
    ''' Terminate a python thread from another thread.
    : param thread: a threading.Thread instance '''

    if not ai_fountain.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_fountain.ident), exc)

    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        '''if it returns a number greater than one, you're in trouble,
        and you should call it again with exc=NULL to revert the effect'''
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_fountain.ident, None)
        raise SystemError("PyThread_SetAsyncExc failed")


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


def get_Weather_URL(base_date, base_time, nx="89", ny="91", numOfRows = "10"):
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


def temperature_check_fountain():
    while True:
        for second in range(60):
            time.sleep(10)
            if randint(0, 10) % 2 == 0:
                sendData = 'a'
                clientSock.send(sendData.encode('utf-8'))
                print("1번 공연장 공연이 개시되오니, 팻말을 확인하세요.")
            elif randint(0, 10) % 2 == 1:
                sendData = 'b'
                clientSock.send(sendData.encode('utf-8'))
                print("2번 공연장 공연이 개시되오니, 팻말을 확인하세요.")
        weather_json = make_weather_json()
        for weather_infomation in weather_json:
            if weather_infomation['category'] == 'T1H' and (weather_infomation['fcstTime'] - weather_infomation['baseTime']) <= 100:
                if int(weather_infomation['fcstValue']) > 20:
                    sendData = 'c'
                    clientSock.send(sendData.encode('utf-8'))
                    recvData = clientSock.recv(1024).decode('utf-8')
                    if recvData == 'c':
                        print("날씨가 더워 분수를 작동시킵니다.")


ai_fountain = threading.Thread(target=temperature_check_fountain)
ai_fountain.daemon = True


def park_opener():

    ai_fountain.start()

    print("공원을 오픈하였습니다!\n")
    time.sleep(1)
    print("이 공원에서는 공연을 열거나 방문객들이 경주를 할 수 있습니다.\n")
    time.sleep(2)
    print("기온이 30도가 넘으면 자동으로 분수가 작동되며\n")
    time.sleep(1)
    print("LED 거리에서는 사람들의 위치에 따라 밝은 조명이 커집니다.\n")

    while True:
        is_exit = input("방문객 경기를 원하시면 숫자를 입력하십시오.\n공원을 닫으시려면 N을 입력하십시오.\n>>>")
        clientSock.send(is_exit.encode('utf-8'))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        if recvData == 'N':
            while ai_fountain.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print('Server notify that server is over')
            clientSock.close()
            print('Client is shutdown')
            return


def simulation():
    situation_case = '''
1. 분수 작동
2. 공연 자동 안내 서비스
3. 공원 내 시설 사용
4. 시뮬레이션 종료
>>>
'''
    print("공원을 가상으로 오픈하였습니다!")
    time.sleep(1)
    print("어떤 동작을 수행하시겠습니까?")
    time.sleep(1)
    while True:
        simul_option = input(situation_case)
        if simul_option == '1':
            sendData = 'c'
            clientSock.send(sendData.encode('utf-8'))
        elif simul_option == '2':
            if randint(0, 10) % 2 == 0:
                sendData = 'a'
                clientSock.send(sendData.encode('utf-8'))
                print("1번 공연장 공연이 개시되오니, 팻말을 확인하세요.")
            elif randint(0, 10) % 2 == 1:
                sendData = 'b'
                clientSock.send(sendData.encode('utf-8'))
                print("2번 공연장 공연이 개시되오니, 팻말을 확인하세요.")
        elif simul_option == '3':
            player_number = input("참가자의 수 >>>")
            clientSock.send(player_number.encode('utf-8'))
        elif simul_option == '4':
            break
        else:
            print("올바른 입력이 아닙니다.")


def web_crawlier(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('tr')

    for tag in tags:
        if tag.find('div'):
            rank = re.compile('<i>(.+)</i>')
            title = re.compile('<b>(.*)<')
            portion = re.compile('<td><b>(.*)</b')
            print('랭킹: %s \t제목: %s\n \t\t\t점유율: %s\n' % (
                rank.search(str(tag)).group(1), title.search(str(tag)).group(1), portion.search(str(tag)).group(1)))
            if rank.search(str(tag)).group(1) == '10':
                break


def show_insight():
    show_menu = '''
1. 전체 공연
2. 뮤지컬
3. 콘서트
4. 연극
>>>    
'''
    show_option = input(show_menu)
    if show_option == '1':
        total_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=P&pCate=&pType=Y&pDate=20181201'
        web_crawlier(total_url)
    elif show_option == '2':
        musical_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=Y&pDate=20181201'
        web_crawlier(musical_url)
    elif show_option == '3':
        concert_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=01003&pCate=&pType=Y&pDate=20181201'
        web_crawlier(concert_url)
    elif show_option == '4':
        play_url = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=01009&pCate=&pType=Y&pDate=20181201'
        web_crawlier(play_url)



server_ip = '192.168.0.7'
port = 8080
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, port))

print('Connecting to the server(%s) on %d port' % (server_ip, port))

menu = '''
1. 공원 개장
2. 시뮬레이션 모드
3. 사용자 모드(공연 빅데이터)
4. 종료
'''


def main():
    while True:
        menu_option = input(menu)
        if menu_option == '1':
            park_opener()
        elif menu_option == '2':
            simulation()
        elif menu_option == '3':
            show_insight()
        elif menu_option == '4':
            clientSock.send('q'.encode('utf-8'))
            recvData = clientSock.recv(1024).decode('utf-8')
            if recvData == 'q':
                print('Server notify that server is over')
                clientSock.close()
                print('Client is shutdown')
            break
        else:
            print("Select the right option!")


if __name__ == "__main__":
    main()
