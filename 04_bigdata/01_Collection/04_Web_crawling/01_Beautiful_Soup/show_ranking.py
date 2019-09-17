from bs4 import BeautifulSoup
import urllib.request
import re
import time

endpoint = 'http://ticket.interpark.com/contents/Ranking/RankList?pKind=P&pCate=&pType=D&pDate='
date = time.strftime("%Y%m%d")

html = urllib.request.urlopen(endpoint+date)
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('tr')

for tag in tags:
    if tag.find('div'):
        rank = re.compile('<i>(.+)</i>')
        title = re.compile('<b>(.*)<')
        portion = re.compile('<td><b>(.*)</b')
        print('랭킹: %s \t제목: %s\n \t\t\t점유율: %s\n' % (rank.search(str(tag)).group(1), title.search(str(tag)).group(1), portion.search(str(tag)).group(1)))
        if rank.search(str(tag)).group(1) == '10':
            break
