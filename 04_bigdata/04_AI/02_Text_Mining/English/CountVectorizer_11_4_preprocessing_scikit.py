# 사용 모델: 싸이키런(sklearn) - LogisticRegression
# 고정 변수 항목: 형태소에서 추출된 단어 빈도
# 분석 목표(예측 값): 스팸 메일 판별
# 데이터 출처 : 캘리포니아 어바인 대학교

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

spam_header = 'spam\t'
no_spam_header = 'ham\t'
documents = []
labels = []

with open('SMSSpamCollection', 'r', encoding='UTF8') as file_handle:
    for line in file_handle:
        # 각줄에서 레이블 부분만 떼어내고 나머지를 documents에 넣는다.
        if line.startswith(spam_header):
            labels.append(1)
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            labels.append(0)
            documents.append(line[len(no_spam_header):])

vectorizer = CountVectorizer() # 단어 횟수 피처를 만드는 클래스
term_counts = vectorizer.fit_transform(documents) # 문서에서 단어 횟수를 센다.
vocabulary = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성된다
# TF: Term Frequency (문서상 발견된 단어) / (전체 문서상의 단어)
# IDF: Inverse Document Frequency
# 주요언어 : is, of, that 같은 단어는 제외하고 빈도를 측정한다.

tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)

# 처리된 파일을 저장합니다. 앞으로의 예제에서 사용될 예정입니다.
with open('processed.pickle', 'wb') as file_handle:
    pickle.dump((vocabulary, features, labels), file_handle)
