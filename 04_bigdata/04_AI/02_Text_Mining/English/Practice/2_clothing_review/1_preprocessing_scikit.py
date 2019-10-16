# 사용 모델 : 싸이키런(sklearn)
# 고정 변수 항목 : 상품에 대한 리뷰, 단어 빈도
# 분석 목표(예측 값) : 상품의 추천 여부

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd

reviews = pd.read_csv('womens_clothing_reviews.csv')

recommended = '1'  # 상품에 대해 추천하면 1
no_recommended = '0'  # 추천하지 않으면 0
user_reviews = []
labels = []

for line in range(len(reviews)):
    if not str(reviews['Review Text']):  # 리뷰가 없을 때 리스트에 저장하지 않음
        continue
    elif str(reviews['Recommended IND'][line]) == recommended:
        labels.append(1)
        user_reviews.append(str(reviews['Review Text'][line]))
    elif str(reviews['Recommended IND'][line]) == no_recommended:
        labels.append(0)
        user_reviews.append(str(reviews['Review Text'][line]))

vectorizer = CountVectorizer()  # 단어 횟수 피처를 만드는 클래스
words_counts = vectorizer.fit_transform(user_reviews)  # 리뷰에서 단어 횟수 세기
voca = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성

tf_transformer = TfidfTransformer(use_idf=False).fit(words_counts)
features = tf_transformer.transform(words_counts)

# 처리된 파일을 저장
with open('processed_review.pickle', 'wb') as file_handle:
    pickle.dump((voca, features, labels), file_handle)
