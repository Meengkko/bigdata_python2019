import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('processed.pickle', 'rb') as file_handle:
    vocabulary, features, labels = pickle.load(file_handle)

# 테스트를 위한 데이터 분류(트레이닝 데이터 추출)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=1)

classifier = LogisticRegression()
classifier.fit(train_features, train_labels)
print('train accuracy: %4.4f' % classifier.score(train_features, train_labels))
print('test accuracy: %4.4f' % classifier.score(test_features, test_labels))

# 단어 빈도수에 따른 우선순위 추출
weights = classifier.coef_[0, :]
pairs = []
for index, value in enumerate(weights):
    pairs.append((abs(value), vocabulary[index]))
pairs.sort(key=lambda x: x[0], reverse=True)
for pair in pairs[:20]:
    print('score %4.4f word: %s' % pair)
