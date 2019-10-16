import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('pre_movie_review.pickle', 'rb') as file:
    voca, features, labels = pickle.load(file)

# 학습 전용, 테스트 전용, 데이터 분리
train_data, test_data, train_label, test_label = train_test_split(features, labels)

# 학습
clf = LogisticRegression()  # clf(classifier)
clf.fit(train_data, train_label)

print('학습 데이터 정확도\t: %.2f' % clf.score(train_data, train_label))
print('테스트 데이터 정확도\t: %.2f' % clf.score(test_data, test_label))

# 어떤 항목이 판별에 영향을 많이 줬는지 알아보기
weights = clf.coef_[0, :]
pair = []
for index, value in enumerate(weights):
    pair.append((abs(value), voca[index]))
pair.sort(key=lambda x: x[0], reverse=True)
for elements in pair[: 25]:
    print('가중치 : %.4f, 단어 : %s' % elements)





