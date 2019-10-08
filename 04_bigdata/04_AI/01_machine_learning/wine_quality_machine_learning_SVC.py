# 머신러닝 모델: SVC
# 독립변수 최적화 분석 결과
# 총 조합 갯수: 562
# MAX 조합: fixed_acidity citric_acid residual_sugar free_sulfur_dioxide total_sulfur_dioxide pH alcohol >> 87.77 %
# 소요된 시간 >>> 1419.78 sec

import pandas as pd
from sklearn import metrics, svm
import operator
from itertools import combinations
import timeit

match_dic = {}

start_time = timeit.default_timer()

print("결과 예측하기")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
wine = wine[wine['type'] == 'white']
wine.drop('type', axis=1, inplace=True)

columns_list = list(wine.columns)
columns_list.remove('quality')
label = wine['quality']
label = label.reset_index(drop="true")


# 최적의 독립변수 실별
for num in range(7, 12):
    combi_list = list(combinations(columns_list, num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC()
        clf.fit(wine[data_header_list], label)
        pre = clf.predict(wine[data_header_list])
        accuracy = metrics.accuracy_score(label, pre)
        data_header_name = ' '.join(data_header_list)
        match_dic[data_header_name] = accuracy * 100
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 정답률: {accuracy * 100}%')


# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)

print("\n\n독립변수 최적화 분석 결과")
print("총 조합 갯수: %d" % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))

end_time = timeit.default_timer()
algor_time = end_time - start_time
print(f'소요된 시간 >>> {round(algor_time, 2)} sec')
