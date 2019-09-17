import urllib.request
import csv
from bs4 import BeautifulSoup
import re


html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

signer = {'up': 1, 'down': -1, 'na': 0}

title_seeker = re.compile(r'<a href="/movie/bi/mi/basic.nhn[?]code=.*title="(.*)">.*</a>', re.MULTILINE)
sign_seeker = re.compile(r'alt="(.*)".*class="arrow"', re.MULTILINE)
variation_seeker = re.compile(r'<td class="range ac">([\d])</td>', re.MULTILINE)
title_list = title_seeker.findall(str(soup))
sign_list = sign_seeker.findall(str(soup))
variation_list = variation_seeker.findall(str(soup))
title_list = title_list[:50]
variation_list = variation_list[1:]
Rank_diff = list(map(lambda x, y: int(x) * signer[y], variation_list, sign_list))
final_list = [['순위', '영화명', '변동폭']]
for i in range(0, 50):
    final_list.append([i+1, title_list[i], Rank_diff[i]])

with open('네이버_영화_실시간_순위_정규표현식.csv', 'w', newline="") as naver_rank:
    csvwriter = csv.writer(naver_rank)
    for row in final_list:
        csvwriter.writerow(row)
