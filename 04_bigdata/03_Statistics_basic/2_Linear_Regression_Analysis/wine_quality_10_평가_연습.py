# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# <= 아래 코드의 의미를 쓰기
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

match_dic = {}

# <= 아래 코드의 의미를 쓰기
columns_list = list(wine.columns)
columns_list.remove('type')
columns_list.remove('quality')


# <= 아래 코드의 의미를 쓰기 (전체 의미와 첫 번째 for문)
for num in range(1,12):
    combi_list = list(combinations(columns_list, num))
    for tup in combi_list:

        # <= 아래 문단의 의미를 쓰기
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')

        # <= 아래 라인의 의미를 쓰기
        lm = ols(my_formula, data=wine).fit()

        dependent_variable = wine['quality']
        independent_variables = wine[list(tup)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = list(map(round, y_predicted))

        match_count = 0
        for index in range(len(dependent_variable)):
            if dependent_variable[index] == y_predicted_rounded[index]:
                match_count += 1
        formula_candid = my_formula.replace('quality ~ ', '')
        match_rate = match_count/len(dependent_variable) * 100

        print('\n>> ' + formula_candid)
        print('>> match count=', match_count)
        print('>> 정답률: %.2f %%'% match_rate )
        match_dic[formula_candid] = match_rate


# <== 아래 라인 의미 쓰기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
