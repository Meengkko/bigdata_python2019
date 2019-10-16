import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('processed_review.pickle', 'rb') as file_handle:
    voca, features, labels = pickle.load(file_handle)

# 학습 전용, 테스트 전용, 데이터 분리
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

# 학습
clf = LogisticRegression()
clf.fit(train_features, train_labels)

print('-'*50)
print('학습 데이터 정확도\t: %.4f' % clf.score(train_features, train_labels))
print('테스트 데이터 정확도\t: %.4f' % clf.score(test_features, test_labels))

# 어떤 항목이 판별에 영향을 많이 줬는지 알아보기
weights = clf.coef_[0, :]
weights_and_words = []
for index, value in enumerate(weights):
    weights_and_words.append((abs(value), voca[index]))
weights_and_words.sort(key=lambda x: x[0], reverse=True)
for elements in weights_and_words[: 25]:
    print('가중치 : %.4f, 단어 : %s' % elements)





