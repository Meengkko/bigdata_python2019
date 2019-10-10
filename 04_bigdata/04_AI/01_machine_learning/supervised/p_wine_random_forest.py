import pandas as pd
import matplotlib.pyplot as plt

from seaborn import heatmap
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

wine_df = pd.read_csv('winequality-both.csv')
wine_df.drop('type', axis=1, inplace=True)

fig, ax = plt.subplots(figsize=(15, 15))
heatmap(wine_df.corr(), ax=ax, cmap='coolwarm')
plt.show()

wine_label = wine_df['quality']
wine_data = wine_df.drop('quality', axis=1)

train_data, test_data, train_label, test_label = train_test_split(wine_data, wine_label)

clf = RandomForestClassifier()
clf.fit(train_data, train_label)
prediction = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, prediction)
cl_report = metrics.classification_report(test_label, prediction)
print("accuracy:", ac_score)
print("report  :\n", cl_report)
