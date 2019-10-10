import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

data_set = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)

neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(data_set)
distances, indices = nbrs.kneighbors(data_set)
distances = np.sort(distances, axis=0)
distances = distances[:, 1]
plt.plot(distances)
plt.show()


model = DBSCAN(min_samples=5, eps=.3)
predict = pd.DataFrame(model.fit_predict(data_set))
predict.columns = ['predict']
predict.index = data_set.index
r = pd.concat([data_set, predict], axis=1)

r.to_excel('DBscan.xlsx', encoding='utf-8')
