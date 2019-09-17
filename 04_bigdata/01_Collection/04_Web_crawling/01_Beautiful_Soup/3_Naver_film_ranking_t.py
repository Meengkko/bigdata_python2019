from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})
up_downs =  soup.findAll('img', attrs={'class':'arrow'})
ranks = soup.findAll('img', attrs={'width':'14'})
ranges = soup.findAll('td', attrs={'class':'range ac'})

f = open('movie_rank_test.csv', 'w', encoding='utf-8')
f.write('rank, name, range\n')
i = 0
while i < len(ranks)-1:
    print('{0}, {1}, {2}, {3}'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    f.write('{0}, {1}, {2}, {3}\n'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    i += 1
f.close()
