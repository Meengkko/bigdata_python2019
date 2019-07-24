#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import datetime
import json

client_id = "Vjvd8HP968mx9tqaryf0"
client_secret = "YzJKAHCn_q"


body = "{\"startDate\":\"2019-01-01\",\"endDate\":\"2019-06-30\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"여성의류\",\"param\":[\"50000167\"]},{\"name\":\"여성언더웨어/잠옷\",\"param\":[\"50000168\"]}],\"device\":\"pc\",\"gender\": \"m\"}";

def get_request_url(url, body):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")
    try:
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        if response.getcode() == 200:
            print("[%s] Url:%s ==> Request Success" % (datetime.datetime.now(), url))
        return response.read().decode('utf8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

'''
def getOption:
    url = "https://openapi.naver.com/v1/datalab/shopping/categories"
'''

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    # print(response.read().decode('utf8'))
else:
    print("Error Code:" + rescode)
