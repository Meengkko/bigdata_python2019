import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from itertools import combinations
import timeit

start = timeit.default_timer()

# 붓꽃의 csv 데이터 읽어 들이기
csv = pd.read_csv('churn.csv')
del csv['State']
del csv['Phone']

csv.loc[csv["Int'l Plan"] == "yes", "Int'l Plan"] = 1
csv.loc[csv["Int'l Plan"] == "no", "Int'l Plan"] = 0

csv.loc[csv["VMail Plan"] == "yes", "VMail Plan"] = 1
csv.loc[csv["VMail Plan"] == "no", "VMail Plan"] = 0

csv_label_case = csv["Churn?"]
csv_data_candid = csv[list(csv.columns)[:-1]]

max_rate = 0
max_combination = []

for num in range(2, len(csv.columns)):
    csv_data_list = list(combinations(csv_data_candid, num))
    for csv_data_case in csv_data_list:
        csv_data_case = csv[list(csv_data_case)]
        train_data, test_data, train_label, test_label = train_test_split(csv_data_case, csv_label_case)
        clf = svm.SVC()
        clf.fit(train_data, train_label)
        pre = clf.predict(test_data)

        ac_score = metrics.accuracy_score(test_label, pre)
        if ac_score > max_rate:
            max_rate = ac_score
            max_combination = list(csv_data_case)
        print("선택된 변수 :", list(csv_data_case))
        print("정답률 =", ac_score)
        print("최고 정답률: %f" % max_rate)
        print("최고 정답률 변수 리스트: ", max_combination)

stop = timeit.default_timer()
print("코드 실행시간:", (stop - start))
