import threading
import time
import ctypes
import urllib.request
import json
import datetime
import urllib.parse
from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET


access_key_dust = "YJnH%2FzEygxtOA3TfMABTPh%2FZ4Ig8dbEI%2FJ%2B2wvfh%2B%2FG4BoUzdVieV0YMyKRc7MEMcE9OcxfXZJ5gUouMZ2Sw6g%3D%3D"


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


def get_dust_url():
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



tree = get_dust_url()
root_node = ET.fromstring(tree)

for station in root_node.find('body').find('items').getiterator('item'):
    if station.findtext("stationName") == '신암동':
        print("%s" % station.findtext('stationName'))
        print("%s" % station.findtext('dataTime'))
        print("%s" % station.findtext('so2Value'))
        print("%s" % station.findtext('no2Value'))
        print("%s" % station.findtext('pm10Grade1h'))
        print("%s" % station.findtext('pm25Grade1h'))
