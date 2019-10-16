import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html, 'html.parser')

tags=soup.find_all('td')

print(str(tags))

'''
title=re.compile('title=.*["][>](.*)</a>')
t=title.findall(str(tags))


range_ac=re.compile('range ac["][>]([\d]{1,2})</td')
r=range_ac.findall(str(tags))


up_down=re.compile('img alt[=]["]([a-z]{2,4})["]')
u=up_down.findall(str(tags))


note_pad = open('Naver_Ranking_ver2','w',encoding='utf8')
note_pad.write("순위|\t영화명\t|\t변동폭\n")
for num in range(0, len(t)):
    if u[num]=='na':
        u[num]=' '
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))
    elif u[num]=='up':
        u[num]='+'
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))
    elif u[num]=='down':
        u[num]='-'
        note_pad.write(" %s\t|\t%s\t|\t%s%s\n"%(num+1,t[num],u[num],r[num]))

print("end")
'''