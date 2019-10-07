# 1. 웹크롤링에 필요한 2가지 모듈 호출
from urllib.request import urlopen # 특정 웹서버에 접근
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석

### I. 1쪽 리뷰만 긁고 출력하기
# 2. 다음 영화소개홈페이지 중 1번째 고객리뷰에접속
url = 'http://movie.daum.net/moviedb/grade?movieId=97728&type=netizen&page=1'
webpage = urlopen(url)
# 3. 댓글 페이지 html 구조 긁어오기
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
# 4. 네티즌 댓글부분(태그:p , 속성명:class, 속성값:desc_review)만 내용 추출하기
reviews = source.findAll('p', {'class': 'desc_review'})

# 5. 네티즌 별로 댓글 줄바꿔 출력하기
for review in reviews:
    print(review.get_text().strip())


### II. 1-10 쪽 리뷰 댓글 긁고, 텍스트파일에 저장하기

review_list=[]
for n in range(10):
    url = 'http://movie.daum.net/moviedb/grade?movieId=97728&type=netizen&page={}'.format(n+1)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage,'html.parser',from_encoding='utf-8')
    reviews = source.findAll('p',{'class': 'desc_review'})

    for review in reviews:
        review_list.append(review.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

# 텍스트파일에 댓글 저장하기
file = open('okja1.txt','w',encoding='utf-8')

for review in review_list:
    file.write(review+'\n')

file.close()
