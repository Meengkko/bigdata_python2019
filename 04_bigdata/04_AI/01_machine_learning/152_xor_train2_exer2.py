import pandas as pd
from sklearn import svm, metrics  # SVM(Support Vector Machine)

or_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
or_df = pd.DataFrame(or_input)
or_data = or_df.iloc[:, 0:2]
or_label = or_df.iloc[:, 2]

# 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(or_data, or_label)
pre = clf.predict(or_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(or_label, pre, normalize=True)
print("정답률 =", ac_score)
