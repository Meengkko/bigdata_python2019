import pandas as pd
from sklearn import preprocessing


def normalize_column(column_name):
    float_array = data_set_tobe_norm[column_name]
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled_array = min_max_scaler.fit_transform(float_array)
    data_set_tobe_norm[column_name] = scaled_array


data_set_tobe_norm = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)
data_list_norm = ['song_old', 'song_weak', 'bae_old', 'bae_weak', 'gup_old', 'gup_weak', 'flow_rate', 'recovery_rate', 'predict']

for col_name in data_list_norm:
    normalize_column(col_name)

print(data_set_tobe_norm.head(10))
print(data_set_tobe_norm.index)

