from gensim.summarization.summarizer import summarize
from newspaper import Article

url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=055&aid=0000765330&date=20191015&type=1&rankingSeq=9&rankingSectionId=103'
news = Article(url, language='ko')
news.download()
news.parse()
print(summarize(news.text, word_count=50, ratio=0.1))
