import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

data_set = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)

fig, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(data_set.corr(), ax=ax, cmap='coolwarm')
plt.show()

'''
# 엘보우 메소드
Sum_of_squared_distances = []
K = range(1, 15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data_set)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()
'''


# silhouette 메소드
for n_clusters in range(2, 10):
    clusterer = KMeans(n_clusters=n_clusters)
    preds = clusterer.fit_predict(data_set)
    centers = clusterer.cluster_centers_

    score = silhouette_score (data_set, preds, metric='euclidean')
    print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))


kmeans = KMeans(n_clusters=3, algorithm='auto')
kmeans.fit(data_set)
predict = pd.DataFrame(kmeans.predict(data_set))
predict.index = data_set.index
predict.columns = ['predict']

r = pd.concat([data_set, predict], axis=1)

plt.scatter(r['area_per_capita'], r['college_grad'], c=r['predict'], alpha=0.5)
plt.show()
plt.scatter(r['apt'], r['song_weak'], c=r['predict'], alpha=0.5)
# centers = pd.DataFrame(kmeans.cluster_centers_, columns=['area_per_capita', 'college_grad'])
# center_x = centers['area_per_capita']
# center_y = centers['college_grad']
# plt.scatter(center_x, center_y, s=50, marker='D', c='r')
plt.show()

r.to_excel("clustered.xlsx", encoding='utf-8')

