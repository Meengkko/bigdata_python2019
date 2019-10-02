# 통계 모델:
# 목표 정답률:
'''
import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# <= 아래 코드의 의미를 쓰기
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# <= 아래 코드의 의미를 쓰기
colums_list = []

# <= 아래 코드의 의미를 쓰기 (전체 의미와 첫 번째 for문)
for num in range(1,12):
    combi_list = list(combinations(,))
    for tup in combi_list:

        # <= 아래 문단의 의미를 쓰기
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')

        # <= 아래 라인의 의미를 쓰기
        lm = ols(my_formula, data=wine).fit()

#        dependent_variable =
#        independent_variables =
#        y_predicted = lm.predict()
#        y_predicted_rounded =
#
#        for index in range()):
#            if :
#                pass
#        print('\n>> '+my_formula.replace('quality ~ ',''))
#        print('>> match count=',)
#        print('>> 정답률: %.2f %%'%())
#        match_dic[] =


# <== 아래 라인 의미 쓰기
match_dic = sorted(, key=operator.itemgetter(),)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len())
print("MAX 조합: %s >> %.2f %%"%(match_dic[][],match_dic[][]))
'''

