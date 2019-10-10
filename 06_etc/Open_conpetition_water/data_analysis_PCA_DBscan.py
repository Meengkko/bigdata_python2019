import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

data_set = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)

index_list = list(data_set.index)

pca = PCA(n_components=3)
principalComponents = pca.fit_transform(data_set)
principalDataframe = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2', 'PC3'])

variables = pd.DataFrame(pca.components_.T)
variables.index = list(data_set.columns)
variables.columns = ['PC1', 'PC2', 'PC3']
variables.to_csv('eigenvalue_PCA.csv', encoding='utf-8')

'''
percent_variance = np.round(pca.explained_variance_ratio_ * 100, decimals=2)
columns = ['PC1', 'PC2', 'PC3']
plt.bar(x=range(1, 4), height=percent_variance, tick_label=columns)
plt.ylabel('Percentate of Variance Explained')
plt.xlabel('Principal Component')
plt.title('PCA Scree Plot')
plt.show()

plt.scatter(principalDataframe.PC1, principalDataframe.PC2)
plt.title('PC1 against PC2')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

plt.scatter(principalDataframe.PC1, principalDataframe.PC3)
plt.title('PC1 against PC3')
plt.xlabel('PC1')
plt.ylabel('PC3')
plt.show()
'''

neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(data_set)
distances, indices = nbrs.kneighbors(data_set)

distances = np.sort(distances, axis=0)
distances = distances[:, 1]
plt.plot(distances)
plt.show()


data_3dim = principalDataframe
data_3dim.fillna(0, inplace=True)
data_3dim.to_excel('debug.xlsx', encoding='utf-8')
print(data_3dim.tail(10))
model = DBSCAN(min_samples=5, eps=.45)
predict = pd.DataFrame(model.fit_predict(data_3dim))
predict.columns = ['predict']
r = pd.concat([data_3dim, predict], axis=1)
r.index = index_list

fig = plt.figure(figsize=(6, 6))
ax = Axes3D(fig, rect=[0.0, 0.0, .95, 1.0], elev=48, azim=134)
ax.scatter(r['PC1'], r['PC2'], r['PC3'], c=r['predict'], alpha=0.5)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
plt.show()

r.to_excel('PCA_DBscan.xlsx', encoding='utf-8')


