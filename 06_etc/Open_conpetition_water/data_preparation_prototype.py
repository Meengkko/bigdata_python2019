import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 아래 모듈은 analysis로 넘어가야한다
import seaborn as sns

data_dir_list = ['d_education', 'd_population', 'd_water_quality', 'd_water_supply']

cities_and_provinces = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
                        '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도',
                        '경상남도', '제주특별자치도']

'''
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

area_per_capita_dir = os.getcwd() + '\\' + "d_area_per_capita"
area_csv_file = ''
for file_name in os.listdir(area_per_capita_dir):
    if file_name.endswith("csv"):
        os.rename(area_per_capita_dir + '\\' + file_name, area_per_capita_dir + '\\' + 'area.csv')
        area_csv_file = 'area.csv'


marriage_age_dir = os.getcwd() + '\\' + "d_marriage_age"
marriage_age_csv_file = ''
for file_name in os.listdir(marriage_age_dir):
    if file_name.endswith("csv"):
        os.rename(marriage_age_dir + '\\' + file_name, marriage_age_dir + '\\' + 'marriage_age.csv')
        marriage_age_csv_file = 'marriage_age.csv'


pipe_dir = os.getcwd() + '\\' + "d_pipe"
pipe_csv_file = ''
for file_name in os.listdir(pipe_dir):
    if file_name.endswith("csv"):
        os.rename(pipe_dir + '\\' + file_name, pipe_dir + '\\' + 'pipe.csv')
        pipe_csv_file = 'pipe.csv'


char_dir = os.getcwd() + '\\' + "d_water_charge"
char_csv_file = ''
for file_name in os.listdir(char_dir):
    if file_name.endswith("csv"):
        os.rename(char_dir + '\\' + file_name, char_dir + '\\' + 'water_charge.csv')
        char_csv_file = 'water_charge.csv'
'''

file_dir_pop = "./d_population/population.csv"
file_dir_edu = "./d_education/education.csv"
file_dir_water = "./d_water_supply/water_sup.csv"
file_dir_area = "./d_area_per_capita/area.csv"
file_dir_ma = "./d_marriage_age/marriage_age.csv"
file_dir_pipe = "./d_pipe/pipe.csv"
file_dir_char = "./d_water_charge/water_charge.csv"

'''
# 수질데이터 중 필요한 정보만 추려서 저장
file_dir_quality = os.getcwd() + '\\' + 'd_water_quality' + '\\' + '월수도꼭지.xlsx'
file_dir_quality.replace("\\", "/")
quality_df = pd.read_excel(file_dir_quality, encoding='cp949')
quality_df = quality_df.iloc[:, [2, -1]]
quality_df.to_excel("./d_water_quality/water_quality.xlsx", encoding='utf-8')
'''


pop_df = pd.read_csv(file_dir_pop, encoding='cp949')
edu_df = pd.read_csv(file_dir_edu, encoding='cp949')
sup_df = pd.read_csv(file_dir_water, encoding='cp949')
quality_df = pd.read_excel("./d_water_quality/water_quality.xlsx")
area_df = pd.read_csv(file_dir_area, encoding='cp949')
ma_df = pd.read_csv(file_dir_ma, encoding='cp949')
pipe_df = pd.read_csv(file_dir_pipe, encoding='cp949')


# 인구 종합정보 데이터 전처리
pop_df = pop_df.drop([0])
pop_df.columns = ["ad_district", "tot_pop", "sex_ratio", "woman_pop", "detached", "apt", "town", "multi", "commercial" ,"other"]

header_list_edu = edu_df.loc[0]
header_list_edu[0] = "ad_district"
edu_df = edu_df.drop([0])
edu_df.columns = header_list_edu

sup_df.rename(columns={'행정구역별': 'ad_district'}, inplace=True)


# 성별, 주거형태 전처리과정
numeric_columns = list(pop_df.columns)[1:]
pop_df[numeric_columns] = pop_df[numeric_columns].apply(pd.to_numeric, errors='coerce')
pop_df = pop_df.fillna(0)

dividend_columns = numeric_columns[1:]
pop_df[dividend_columns] = pop_df[dividend_columns].div(pop_df['tot_pop'], axis=0)
pop_df['sex_ratio'] = pop_df['sex_ratio'].div(pop_df['woman_pop'], axis=0)
pop_df.index = list(pop_df.iloc[:, 0])
pop_df.drop(["ad_district", "tot_pop", 'woman_pop'], axis="columns", inplace=True)
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


# 수질데이터 전처리(잔여염소)
data_dict = {}
quality_dist = list(set(quality_df['행정구역']))
for dist in quality_dist:
    data_dict[f'{dist}'] = {"chlorine": quality_df[quality_df['행정구역'] == f'{dist}'].iloc[:, -1].mean()}

quality_df_mean = pd.DataFrame.from_dict(data_dict, orient='index')


# 도시면적, 녹지면적 데이터 전처리과정
area_df = area_df.drop([0])
area_df.columns = ['dist_1', 'dist_2', 'area_per_capita', 'green_per_capita']
index_list_area = []
for idx, row in area_df.iterrows():
    if row['dist_2'] != '소계':
        index_list_area.append(row['dist_1']+' '+row['dist_2'])
    else:
        index_list_area.append(row['dist_1'])
area_df.index = index_list_area
area_df.drop(['dist_1', 'dist_2'], axis=1, inplace=True)


# 기혼율 정보 데이터 전처리
ma_df.drop(['단위', 'Unnamed: 5'], axis=1, inplace=True)
marriage_df = ma_df[ma_df["연령별"] == "합계"]
marriage_tot = marriage_df[marriage_df["항목"] == "내국인(15세이상)-계"]
marriage_married = marriage_df[marriage_df["항목"] == "내국인-배우자있음"]
tot = marriage_tot["2015 년"].astype("int")
tot = tot.reset_index(drop=True)
married = marriage_married["2015 년"].astype("int")
married = married.reset_index(drop=True)

marriage_rate = married / tot
marriage_rate.index = list(marriage_tot['행정구역별(시군구)'])
marriage_rate.drop(['동부', '읍부', '면부'], axis=0, inplace=True)

ma_index_new = []
current_city = ''
for index in list(marriage_rate.index):
    if index in cities_and_provinces:
        ma_index_new.append(index)
        current_city = index
    elif index == '전국':
        ma_index_new.append(index)
    else:
        ma_index_new.append(current_city+' '+index)
marriage_rate.index = ma_index_new
marriage_rate = marriage_rate.rename("marriage_rate")


# 상수도관 시도별 현황 데이터 전처리
pipe_df = pipe_df[pipe_df["구분별(2)"] == "총계"]
pipe_df.drop([15, 249], axis=0, inplace=True)
pipe_df = pipe_df.iloc[:, [0, 9, 11, 14, 16, 19, 21]]
list_candid = list(pipe_df["구분별(1)"])
list_candid[0] = '전국'
pipe_df.index = list_candid
pipe_df.drop("구분별(1)", axis=1, inplace=True)
pipe_df.columns = ['song_old', 'song_weak', 'bae_old', 'bae_weak', 'gup_old', 'gup_weak']
pipe_df = pipe_df.apply(pd.to_numeric, errors='coerce')


# 유수율, 요금현실화율 시도별 데이터 전처리
char_df = pd.read_csv(file_dir_char, encoding='cp949')
char_df = char_df.iloc[:, [0, 4, 7]]
char_df.drop([0], axis=0, inplace=True)
list_candid_char = list(char_df["시도별(1)"])
list_candid_char[0] = '전국'
char_df.index = list_candid_char
char_df.drop("시도별(1)", axis=1, inplace=True)
char_df.columns = ['flow_rate', 'recovery_rate']
char_df = char_df.apply(pd.to_numeric, errors='coerce')

small_merged_data = pd.merge(pipe_df, char_df, left_index=True, right_index=True, how='left')
sm_data_columns = list(small_merged_data.columns)
dataset_merged = pd.merge(pop_df, edu_df, left_index=True, right_index=True, how='left')
dataset_merged = pd.merge(dataset_merged, sup_df, left_index=True, right_index=True, how='left')
dataset_merged = pd.merge(dataset_merged, quality_df_mean, left_index=True, right_index=True, how='left')
dataset_merged = pd.merge(dataset_merged, area_df, left_index=True, right_index=True, how='left')
dataset_merged = pd.merge(dataset_merged, marriage_rate, left_index=True, right_index=True, how='left')

index_small = list(small_merged_data.index)
for column in sm_data_columns:
    dataset_merged[column] = 0

for small_index, small_row in small_merged_data.iterrows():
    for row_index, merged_row in dataset_merged.iterrows():
        if small_index == row_index.split(' ')[0]:
            dataset_merged.loc[row_index, sm_data_columns] = small_row

fillin_column = ['water_sup', 'chlorine', 'area_per_capita', 'green_per_capita']

for fill_col in fillin_column:
    for city_name in cities_and_provinces:
        if dataset_merged.loc[city_name, fill_col] in [np.nan]:
            continue
        for index in list(dataset_merged.index):
            if str(dataset_merged.loc[index, fill_col]) == 'nan':
                if city_name == index.split(' ')[0]:
                    dataset_merged.loc[index, fill_col] = dataset_merged.loc[city_name, fill_col]

null_average = ['경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도']
for avg_city in null_average:
    num_collector = []
    for index in list(dataset_merged.index):
        if avg_city == index.split(' ')[0]:
            if str(dataset_merged.loc[index, 'chlorine']) == 'nan':
                continue
            num_collector.append(dataset_merged.loc[index, 'chlorine'])
    dataset_merged.loc[avg_city, 'chlorine'] = sum(num_collector) / len(num_collector)

for city_name in null_average:
    for index in list(dataset_merged.index):
        if str(dataset_merged.loc[index, 'chlorine']) == 'nan':
            dataset_merged.loc[index, 'chlorine'] = dataset_merged.loc[city_name, 'chlorine']

dataset_merged = dataset_merged.apply(pd.to_numeric, errors='coerce')

dataset_merged.loc['전국', 'chlorine'] = dataset_merged.loc[:, 'chlorine'].mean()
dataset_merged['middle_grad'].fillna(dataset_merged['middle_grad'].median(), inplace=True)
dataset_merged['high_grad'].fillna(dataset_merged['high_grad'].median(), inplace=True)
dataset_merged['college_grad'].fillna(dataset_merged['college_grad'].median(), inplace=True)
dataset_merged['graduate'].fillna(dataset_merged['graduate'].median(), inplace=True)
dataset_merged['marriage_rate'].fillna(dataset_merged['marriage_rate'].median(), inplace=True)

# 변동성이 높은 변수 로그처리
dataset_merged.loc['인천광역시 옹진군', 'area_per_capita'] = 1
dataset_merged.loc['인천광역시 옹진군', 'green_per_capita'] = 1
dataset_merged['area_per_capita'] = np.log(dataset_merged['area_per_capita'])
dataset_merged['green_per_capita'] = np.log(dataset_merged['green_per_capita'])
dataset_merged['water_sup'] = np.log(dataset_merged['water_sup'])

dataset_merged.drop(cities_and_provinces, axis=0, inplace=True)
dataset_merged.drop('전국', axis=0, inplace=True)

before_cols_save = list(dataset_merged.columns)
before_index_save = list(dataset_merged.index)

# 모든 자료 스케일링(0 ~ 1)
scaler = StandardScaler()
dataset_merged = scaler.fit_transform(dataset_merged)
dataset_merged = pd.DataFrame(dataset_merged)

'''
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
'''
'''

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

fig, ax = plt.subplots(figsize=(16,10))
sns.heatmap(dataset_merged.corr(), ax=ax)
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(dataset_merged)
'''
dataset_merged.columns = before_cols_save
dataset_merged.index = before_index_save
list_total_data = list(dataset_merged.columns)
ratio_data = list_total_data[:11]
rest_of_data = list_total_data[11:]

sns.boxplot(x="variable", y="value", data=pd.melt(dataset_merged[ratio_data]))
plt.show()

sns.boxplot(x="variable", y="value", data=pd.melt(dataset_merged[rest_of_data]))
plt.show()

dataset_merged.to_excel("test_ver1.01.xlsx", encoding='utf-8')
print("save_accomplished")

