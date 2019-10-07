import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# 아래 모듈은 analysis로 넘어가야한다
import seaborn as sns
from sklearn.cluster import KMeans


data_dir_list = ['d_education', 'd_population', 'd_water_quality', 'd_water_supply']

population_dir = os.getcwd() + '\\' + data_dir_list[1]
pop_csv_file = ''
for file_name in os.listdir(population_dir):
    if file_name.endswith("csv"):
        os.rename(population_dir + '\\' + file_name, population_dir + '\\' + "population.csv")
        pop_csv_file = "population.csv"

education_dir = os.getcwd() + '\\' + data_dir_list[0]
education_csv_file = ''
for file_name in os.listdir(education_dir):
    if file_name.endswith("csv"):
        os.rename(education_dir + '\\' + file_name, education_dir + '\\' + "education.csv")
        education_csv_file = "education.csv"

water_sup_dir = os.getcwd() + '\\' + data_dir_list[3]
water_sup_csv_file = ''
for file_name in os.listdir(water_sup_dir):
    if file_name.endswith("csv"):
        os.rename(water_sup_dir + '\\' + file_name, water_sup_dir + '\\' + "water_sup.csv")
        water_sup_csv_file = "water_sup.csv"


file_dir_pop = (population_dir + "\\" + pop_csv_file)
file_dir_edu = (education_dir + "\\" + education_csv_file)
file_dir_water = (water_sup_dir + "\\" + water_sup_csv_file)
file_dir_pop.replace("\\", "/")
file_dir_edu.replace("\\", "/")
file_dir_water.replace("\\", "/")

pop_df = pd.read_csv(file_dir_pop, encoding='cp949')
edu_df = pd.read_csv(file_dir_edu, encoding='cp949')
sup_df = pd.read_csv(file_dir_water, encoding='cp949')


pop_df = pop_df.drop([0])
pop_df.columns = ["ad_district", "tot_pop", "man_pop", "woman_pop", "detached", "apt", "town", "multi", "commercial" ,"other"]

header_list_edu = edu_df.loc[0]
header_list_edu[0] = "ad_district"
edu_df = edu_df.drop([0])
edu_df.columns = header_list_edu

sup_df.rename(columns={'행정구역별': 'ad_district'}, inplace=True)


cities_and_provinces = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
                        '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도',
                        '경상남도', '제주특별자치도']

# 성별, 주거형태 전처리과정
numeric_columns = list(pop_df.columns)[1:]
pop_df[numeric_columns] = pop_df[numeric_columns].apply(pd.to_numeric, errors='coerce')
pop_df = pop_df.fillna(0)

dividend_columns = numeric_columns[1:]
pop_df[dividend_columns] = pop_df[dividend_columns].div(pop_df['tot_pop'], axis=0)
pop_df.index = list(pop_df.iloc[:, 0])
pop_df.drop(["ad_district", "tot_pop"], axis="columns", inplace=True)
pop_df.drop(['읍부', '면부', '동부'], axis=0, inplace=True)

index_list = list(pop_df.index)
amend_list = []
current_city = ''
for city_name in index_list:
    if city_name in cities_and_provinces:
        amend_list.append(city_name)
        current_city = city_name
    elif city_name == '전국':
        amend_list.append('전국')
    else:
        amend_list.append(current_city + ' ' + city_name)

pop_df.index = amend_list

# 학력수준 전처리과정
edu_df.index = list(edu_df.iloc[:, 0])
edu_df.drop(['ad_district', '성별', '연령별'], axis='columns', inplace=True)
edu_df = edu_df.apply(pd.to_numeric, errors='coerce')
edu_df = edu_df.fillna(0)
sum_dict = {"middle_grad": [1, 5, 11, 12, 35], "high_grad": [10, 15, 16, 17, 18, 21, 22, 23, 24], "college_grad": [14, 20, 27, 28, 29], "graduate": [26, 30]}

for sum_name in sum_dict.keys():
    edu_df[sum_name] = edu_df.iloc[:, sum_dict[sum_name]].sum(axis=1, skipna=True)

edu_dividend_columns = list(edu_df.columns)[-4:]
edu_drop_columns = list(edu_df.columns)[:-4]

edu_df[edu_dividend_columns] = edu_df[edu_dividend_columns].div(edu_df.iloc[:, 0], axis=0)
edu_df.drop(edu_drop_columns, axis='columns', inplace=True)
edu_df.drop(['읍부', '면부', '동부'], axis=0, inplace=True)

index_list = list(edu_df.index)
amend_list = []
current_city = ''
for city_name in index_list:
    if city_name in cities_and_provinces:
        amend_list.append(city_name)
        current_city = city_name
    elif city_name == '전국':
        amend_list.append('전국')
    else:
        amend_list.append(current_city + ' ' + city_name)

edu_df.index = amend_list


# 상수도 보급률 전처리과정
sup_df.index = list(sup_df.iloc[:, 0])
sup_df.drop(['ad_district'], axis='columns', inplace=True)
sup_df = sup_df.apply(pd.to_numeric, errors='coerce')
sup_df.columns = ['water_sup']

index_list = list(sup_df.index)
amend_list = []
current_city = ''
for city_name in index_list:
    if city_name in cities_and_provinces:
        amend_list.append(city_name)
        current_city = city_name
    elif city_name == '전국':
        amend_list.append('전국')
    else:
        amend_list.append(current_city + ' ' + city_name)

sup_df.index = amend_list

dataset_merged = pd.merge(pop_df, edu_df, left_index=True, right_index=True, how='left')
dataset_merged = pd.merge(dataset_merged, sup_df, left_index=True, right_index=True, how='left')

# 지역별 교육수준 박스플롯
plt.subplot(2, 2, 1)
plt.boxplot(dataset_merged['middle_grad'].dropna(), vert=False, showmeans=True)
plt.title('middle_grad')

plt.subplot(2, 2, 2)
plt.boxplot(dataset_merged['high_grad'].dropna(), vert=False, showmeans=True)
plt.title('high_grad')

plt.subplot(2, 2, 3)
plt.boxplot(dataset_merged['college_grad'].dropna(), vert=False, showmeans=True)
plt.title('college_grad')

plt.subplot(2, 2, 4)
plt.boxplot(dataset_merged['graduate'].dropna(), vert=False, showmeans=True)
plt.title('graduate')

plt.show()

dataset_merged['middle_grad'].fillna(dataset_merged['middle_grad'].median(), inplace=True)
dataset_merged['high_grad'].fillna(dataset_merged['high_grad'].median(), inplace=True)
dataset_merged['college_grad'].fillna(dataset_merged['college_grad'].median(), inplace=True)
dataset_merged['graduate'].fillna(dataset_merged['graduate'].median(), inplace=True)


# 상수도 보급률 히스토그램, 박스 플롯

plt.hist(sup_df['water_sup'], histtype='bar', rwidth=0.9)
plt.xlabel('supply_rate')
plt.ylabel('frequency')
plt.title('Histogram of supply rate')
plt.show()

plt.figure(figsize=(7, 6))
boxplot = sup_df.boxplot(column=['water_sup'])
plt.show()

dataset_merged['water_sup'].fillna(dataset_merged['water_sup'].median(), inplace=True)
# dataset_merged.to_excel("test.xlsx", encoding='utf-8')

'''
fig, ax = plt.subplots(figsize=(16,10))
sns.heatmap(dataset_merged.corr(), ax=ax)
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(dataset_merged)
'''
