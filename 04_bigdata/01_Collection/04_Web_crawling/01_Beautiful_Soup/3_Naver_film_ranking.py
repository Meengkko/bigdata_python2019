import urllib.request
import csv
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

rank = 1
rank_list = [['순위', '영화명', '변동폭']]
signer = {'up': 1, 'down': -1, 'na': 0}
tags = soup.findAll('tr')
for tag in tags:
    if tag.find('a'):
        rank_list.append([rank, tag.find('a').text, signer[tag.find('img', attrs={'class':'arrow'}).attrs['alt']]*int(tag.find('td', attrs={'class': 'range ac'}).text)])
        rank = rank + 1

with open('네이버_영화_실시간_순위.csv', 'w', newline="") as naver_rank:
    csvwriter = csv.writer(naver_rank)
    for row in rank_list:
        csvwriter.writerow(row)
