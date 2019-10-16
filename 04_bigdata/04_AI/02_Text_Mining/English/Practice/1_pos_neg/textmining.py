import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

documents = []
labels = []

file_list_neg = os.listdir("./neg")
for a in range(len(file_list_neg)):
    labels.append(0)  # 부정적인 평가의 라벨
for a in file_list_neg:
    with open('./neg/%s' % a, 'r', encoding='UTF8') as fp:
        k = fp.read()
        documents.append(k)

file_list_pos = os.listdir("./pos")
for a in range(len(file_list_pos)):
    labels.append(1)  # 부정적인 평가의 라벨
for a in file_list_pos:
    with open('./pos/%s' % a, 'r', encoding='UTF8') as fp:
        k = fp.read()
        documents.append(k)

vectorizer = CountVectorizer()  # 단어 횟수 피처를 만드는 클래스
term_counts = vectorizer.fit_transform(documents)  # 문서에서 단어 횟수를 센다
vocabulary = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성

tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)

# 전처리한 파일 생성
with open('processed.pickle', 'wb') as file_handle:
    pickle.dump((vocabulary, features, labels), file_handle)

classifier = LogisticRegression()
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)
classifier.fit(train_features, train_labels)
print('train accuracy: %4.4f' % classifier.score(train_features, train_labels))
print('test accuracy: %4.4f' % classifier.score(test_features, test_labels))

# 어떤 항목이 판별에 영향을 많이 줬는지 찾아보기
weights = classifier.coef_[0, :]
pairs = []
for index, value in enumerate(weights):
    pairs.append((abs(value), vocabulary[index]))
pairs.sort(key=lambda x: x[0], reverse=True)
for pair in pairs[: 20]:
    print('score %4.4f word: %s' % (pair[0], pair[1]))



