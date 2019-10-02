import pandas as pd
from sklearn import svm, metrics

csv_df = pd.read_csv('iris.csv')
csv_data = list(csv_df.columns)[:-1]
csv_label = csv_df((csv_df.columns)[-1])




