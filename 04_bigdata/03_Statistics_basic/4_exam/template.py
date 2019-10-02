# 통계 모델: 선형회귀 분석 (Linear Regression Analysis)
# 목표 정답률: 독립변수를 모두 조합 한 결과 약 53.0244%를 초과한 정답률

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# [문항1]  주어진 데이터를 분석하여 최종적으로 적용 가능한 통계 모델에 대한 가설을 도출하시오
# 데이터 출처: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

# 1) 데이터 불러오기
# 정답: wine = pd.read_csv('winequality-both.csv', sep=',', header=0)

# 데이터 의미 요약: 아래 코드는 데이터의 형태를 출력할 수 있다. & 데이터의 의미에 관하여 적절하게 서술
# print(wine.dtypes)
# 적용가능한 통계 모델: 범주형인 type을 제외하면 정수형인 와인 품질을 설명할 변수후보는 모두 실수형이므로 선형회귀를 적합할 수 있다.


# [문항2]  가설에 따른 빅데이터 모델 구현 코드를 기술 하시오.
# 통계 모델: 다변수 선형회귀 모형
# 독립변수 추출

# 2) 데이터 프레임으로부터 독립변수 가져오기
# 정답: wine.columns = wine.columns.str.replace(' ', '_')

independent_variables = list(wine.columns)
independent_variables.remove('type')
independent_variables.remove('quality')

# 목표 정답률, 통계분석 결과
my_formula = "quality ~ "
for x_i in independent_variables:
    my_formula += f"{x_i} + "
my_formula = my_formula.strip().rstrip('+')

# 3) 모든 독립변수를 포함하여 선형회귀모형 적합하기
# 정답: lm = ols(my_formula, data=wine).fit()
# +  결과해석
# 정답: print(lm.summary())

# 최적의 독립변수 식별
match_dic = {}
for num in range(1, 12):

    # 4) 각 변수의 갯수에 맞는 변수의 조합 추출하기
    # 정답: combi_list = list(combinations(independent_variables, num))

    for tup in combi_list:
        my_formula = 'quality ~ '
        for data in tup:
            my_formula += '%s + ' % data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables_obsv = wine[list(tup)]
        y_predicted = lm.predict(independent_variables_obsv)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0

        # 5) 예측치를 이용하여 정답률 구하기
        # 정답: for index in range(len(y_predicted_rounded)):
        #     if y_predicted_rounded[index] == dependent_variable.values[index]:
        #         match_count += 1

        print('\n>> ' + my_formula.replace('quality ~ ', ''))
        print('>> match count =', match_count)
        print('>> 정답률: %.2f %%' % (match_count/len(y_predicted_rounded)*100))
        match_dic['%s' % my_formula.replace('quality ~ ', '')] = match_count/len(y_predicted_rounded)*100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print("총 조합 갯수: %d" % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))

# [문항3] 구현한 프로그램의 검증 결과를 첨부하시오
# 정답률, 모델 성능 평가 결과를 포함한 수행 결과 첨부
