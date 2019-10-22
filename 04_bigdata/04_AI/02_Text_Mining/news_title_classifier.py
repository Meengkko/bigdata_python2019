import csv
from bayes import BaysianFilter

baysian = BaysianFilter()

csv_file = open('accumulative_news_cat.csv', 'r', encoding='utf-8')
read_csv = csv.reader(csv_file)

for line in read_csv:
    if line:
        baysian.fit(line[1], line[0])

csv_file.close()
news_title = input('뉴스기사 제목을 입력하세요: ')
pre, score_list = baysian.predict(news_title)

print('\n<분석결과>')
print(f'* 카테고리별 평가 점수: {score_list}')
print("* 판정 결과 =", pre)
