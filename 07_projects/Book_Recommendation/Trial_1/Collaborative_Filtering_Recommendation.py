import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation, cosine
import ipywidgets as widgets
from IPython.display import display, clear_output
from sklearn.metrics import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys, os
from contextlib import contextmanager

# M is user-item ratings matrix where ratings are integers from 1-10
M = np.asarray([[3, 7, 4, 9, 9, 7],
                [7, 0, 5, 3, 8, 8],
               [7, 5, 5, 0, 8, 4],
               [5, 6, 8, 5, 9, 8],
               [5, 8, 8, 8, 10, 9],
               [7, 7, 0, 4, 7, 8]])
M = pd.DataFrame(M)

# declaring k,metric as global which can be changed by the user later
k = 4
# can be changed to 'correlation' for Pearson correlation similaries
metric = 'cosine'
cosine_sim = 1-pairwise_distances(M, metric="cosine")


def findksimilarusers(user_id, ratings, metric=metric, k=k):
    similarities = []
    indices = []
    model_knn = NearestNeighbors(metric=metric, algorithm='brute')
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[user_id - 1, :].values.reshape(1, -1), n_neighbors=k + 1)
    similarities = 1 - distances.flatten()
    print('{0} most similar users for User {1}:\n'.format(k, user_id))
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] + 1 == user_id:
            continue

        else:
            print('{0}: User {1}, with similarity of {2}'.format(i, indices.flatten()[i] + 1, similarities.flatten()[i]))

    return similarities, indices


# This function predicts rating for specified user-item combination based on user-based approach
def predict_userbased(user_id, item_id, ratings, metric=metric, k=k):
    prediction = 0
    similarities, indices = findksimilarusers(user_id, ratings, metric, k)  # similar users based on cosine similarity
    mean_rating = ratings.loc[user_id - 1, :].mean()  # to adjust for zero based indexing
    sum_wt = np.sum(similarities) - 1
    product = 1
    wtd_sum = 0

    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] + 1 == user_id:
            continue
        else:
            ratings_diff = ratings.iloc[indices.flatten()[i], item_id - 1] - np.mean(
                ratings.iloc[indices.flatten()[i], :])
            product = ratings_diff * (similarities[i])
            wtd_sum = wtd_sum + product

    prediction = int(round(mean_rating + (wtd_sum / sum_wt)))
    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

    return prediction


# This function finds k similar items given the item_id and ratings matrix M
def findksimilaritems(item_id, ratings, metric=metric, k=k):
    similarities=[]
    indices=[]
    ratings=ratings.T
    model_knn = NearestNeighbors(metric=metric, algorithm='brute')
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[item_id-1, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    print('{0} most similar items for item {1}:\n'.format(k, item_id))
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i]+1 == item_id:
            continue

        else:
            print('{0}: Item {1} :, with similarity of {2}'.format(i, indices.flatten()[i]+1, similarities.flatten()[i]))

    return similarities, indices


# This function predicts the rating for specified user-item combination based on item-based approach
def predict_itembased(user_id, item_id, ratings, metric=metric, k=k):
    prediction = wtd_sum = 0
    similarities, indices = findksimilaritems(item_id, ratings)  # similar users based on correlation coefficients
    sum_wt = np.sum(similarities) - 1
    product = 1

    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] + 1 == item_id:
            continue
        else:
            product = ratings.iloc[user_id - 1, indices.flatten()[i]] * (similarities[i])
            wtd_sum = wtd_sum + product
    prediction = int(round(wtd_sum / sum_wt))
    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

    return prediction


# This function is used to compute adjusted cosine similarity matrix for items
def computeAdjCosSim(M):
    sim_matrix = np.zeros((M.shape[0], M.shape[1]))
    M_u = M.mean(axis=1)  # means

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if i == j:

                sim_matrix[i][j] = 1
            else:
                if i < j:

                    sum_num = sum_den1 = sum_den2 = 0
                    for k, row in M.loc[:, [i, j]].iterrows():

                        if ((M.loc[k, i] != 0) & (M.loc[k, j] != 0)):
                            num = (M[i][k] - M_u[k]) * (M[j][k] - M_u[k])
                            den1 = (M[i][k] - M_u[k]) ** 2
                            den2 = (M[j][k] - M_u[k]) ** 2

                            sum_num = sum_num + num
                            sum_den1 = sum_den1 + den1
                            sum_den2 = sum_den2 + den2

                        else:
                            continue

                    den = (sum_den1 ** 0.5) * (sum_den2 ** 0.5)
                    if den != 0:
                        sim_matrix[i][j] = sum_num / den
                    else:
                        sim_matrix[i][j] = 0


                else:
                    sim_matrix[i][j] = sim_matrix[j][i]

    return pd.DataFrame(sim_matrix)


# This function finds k similar items given the item_id and ratings matrix M

def findksimilaritems_adjcos(item_id, ratings, k=k):
    sim_matrix = computeAdjCosSim(ratings)
    similarities = sim_matrix[item_id - 1].sort_values(ascending=False)[:k + 1].values
    indices = sim_matrix[item_id - 1].sort_values(ascending=False)[:k + 1].index

    print('{0} most similar items for item {1}:\n'.format(k, item_id))
    for i in range(0, len(indices)):
        if indices[i] + 1 == item_id:
            continue

        else:
            print('{0}: Item {1} :, with similarity of {2}'.format(i, indices[i] + 1, similarities[i]))

    return similarities, indices


# This function predicts the rating for specified user-item combination for adjusted cosine item-based approach
# As the adjusted cosine similarities range from -1,+1, sometimes the predicted rating can be negative or greater than max value
# Hack to deal with this: Rating is set to min if prediction is negative, Rating is set to max if prediction is above max
def predict_itembased_adjcos(user_id, item_id, ratings):
    prediction = 0

    similarities, indices = findksimilaritems_adjcos(item_id,
                                                     ratings)  # similar users based on correlation coefficients
    sum_wt = np.sum(similarities) - 1

    product = 1
    wtd_sum = 0
    for i in range(0, len(indices)):
        if indices[i] + 1 == item_id:
            continue
        else:
            product = ratings.iloc[user_id - 1, indices[i]] * (similarities[i])
            wtd_sum = wtd_sum + product
    prediction = int(round(wtd_sum / sum_wt))
    if prediction < 0:
        prediction = 1
    elif prediction > 10:
        prediction = 10
    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

    return prediction


# similarities, indices = findksimilarusers(1, M, metric='cosine')
# similarities, indices = findksimilarusers(1, M, metric='correlation')
# predict_userbased(3, 4, M)
# similarities, indices = findksimilaritems(3, M)
# prediction = predict_itembased(1, 3, M)
# adjcos_sim = computeAdjCosSim(M)
# similarities, indices = findksimilaritems_adjcos(3, M)
prediction = predict_itembased_adjcos(3, 4, M)
