import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


data_set = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)

print(data_set.head())

kmeans = KMeans(n_clusters=4, algorithm='auto')
kmeans.fit(data_set)
predict = pd.DataFrame(kmeans.predict(data_set))
predict.index = data_set.index
predict.columns = ['predict']

print(data_set.head())

r = pd.concat([data_set, predict], axis=1)
print(r.head())

plt.scatter(r['area_per_capita'], r['college_grad'], c=r['predict'], alpha=0.5)
# centers = pd.DataFrame(kmeans.cluster_centers_, columns=['area_per_capita', 'college_grad'])
# center_x = centers['area_per_capita']
# center_y = centers['college_grad']
# plt.scatter(center_x, center_y, s=50, marker='D', c='r')
plt.show()

r.to_excel("clustered.xlsx", encoding='utf-8')

