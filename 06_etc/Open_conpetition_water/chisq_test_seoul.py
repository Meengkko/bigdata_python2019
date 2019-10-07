import pandas as pd
from scipy.stats import chisquare

# 데이터: 성, 연령, 학력, 주택형태, 입주형태, 가구원수, 소득, 지역별 수돗물 음용통계
# 출처: 서울열린데이터광장 [서울시 음용식수 통계 2016년 자료]
# https://data.seoul.go.kr/dataList/datasetView.do?infId=382&srvType=S&serviceKind=2

seoul_tab = pd.read_csv('report.txt', sep='\t')
rate_list = list(seoul_tab.columns)[3:]
rate_list.append('기간')

tab_list = ['수돗물을끓여서마신다', '수돗물을그냥마신다']
non_list = ['수돗물을정수하여마신다', '먹는샘물을사서마신다', '약수지하수를마신다', '기타']

seoul_tab = seoul_tab.replace({'수돗물을그냥마신다': '-'}, {'수돗물을그냥마신다': 0.0})
seoul_tab = seoul_tab.replace({'기타': '-'}, {'기타': 0.0})
seoul_tab['수돗물을그냥마신다'] = seoul_tab['수돗물을그냥마신다'].apply(pd.to_numeric)

seoul_tab['tab_water'] = seoul_tab[tab_list].sum(axis=1)
seoul_tab['non_tab_water'] = seoul_tab[non_list].sum(axis=1)

seoul_tab = seoul_tab.drop(rate_list, axis=1)
seoul_tab.loc[35:59, ['대분류']] = '지역소분류'
print(seoul_tab)

# 카이제곱 검정
tab_rate_by_sex = seoul_tab.loc[seoul_tab['대분류'] == '성별'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_sex, axis=None))

tab_rate_by_ages = seoul_tab.loc[seoul_tab['대분류'] == '연령별'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_ages, axis=None))

tab_rate_by_education = seoul_tab.loc[seoul_tab['대분류'] == '학력별'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_education, axis=None))

tab_rate_by_residence = seoul_tab.loc[seoul_tab['대분류'] == '주택형태'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_residence, axis=None))

tab_rate_by_housing = seoul_tab.loc[seoul_tab['대분류'] == '입주형태'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_housing, axis=None))

tab_rate_by_family = seoul_tab.loc[seoul_tab['대분류'] == '가구원수'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_family, axis=None))

tab_rate_by_income = seoul_tab.loc[seoul_tab['대분류'] == '소득'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_income, axis=None))

tab_rate_by_area = seoul_tab.loc[seoul_tab['대분류'] == '지역대분류'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_area, axis=None))

tab_rate_by_borough = seoul_tab.loc[seoul_tab['대분류'] == '지역소분류'].drop(['대분류', '분류'], axis=1)
print(chisquare(tab_rate_by_borough, axis=None))
