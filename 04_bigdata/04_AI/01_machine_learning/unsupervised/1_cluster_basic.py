import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.cluster, sklearn.preprocessing

alco2009 = pd.read_csv('niaaa-report2009.csv', index_col='State')
states = pd.read_csv('states2.csv', names=("State", "Standard", "Postal", "Capital"))
columns = ['Wine', 'Beer']

kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009['Clusters'] = kmeans.labels_
centers = pd.DataFrame(kmeans.cluster_centers_, columns=columns)

matplotlib.style.use('ggplot')

ax = alco2009.plot.scatter(columns[0], columns[1], c='Clusters', cmap=plt.cm.Accent, s=100)
centers.plot.scatter(columns[0], columns[1], color='red', marker='+', s=200, ax=ax)

plt.title("US States Clustered by Alcohol Consumption")
plt.savefig("clusters.pdf")
