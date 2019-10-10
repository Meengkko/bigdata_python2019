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

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(data_set)
principalDataframe = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])

variables = pd.DataFrame(pca.components_.T)
variables.index = list(data_set.columns)
variables.columns = ['PC1', 'PC2']
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


data_2dim = principalDataframe
model = DBSCAN(min_samples=8, eps=.35)
predict = pd.DataFrame(model.fit_predict(data_2dim))
predict.columns = ['predict']
r = pd.concat([data_2dim, predict], axis=1)
r.index = index_list

plt.scatter(r['PC1'], r['PC2'], c=r['predict'], alpha=0.5)
plt.show()
r.to_excel('PCA_DBscan.xlsx', encoding='utf-8')
