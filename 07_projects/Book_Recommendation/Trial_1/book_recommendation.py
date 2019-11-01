# Making necessary imports
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation
from sklearn.metrics.pairwise import pairwise_distances
import ipywidgets as widgets
from IPython.display import display, clear_output
from contextlib import contextmanager
import warnings
warnings.filterwarnings('ignore')
import os, sys
import re
import seaborn as sns

from sklearn.neighbors import NearestNeighbors

books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding='latin-1')
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']

users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding='latin-1')
users.columns = ['userID', 'Location', 'Age']

ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding='latin-1')
ratings.columns = ['userID', 'ISBN', 'bookRating']

print(books.shape)
print(users.shape)
print(ratings.shape)

books.drop(['imageUrlS', 'imageUrlM', 'imageUrlL'], axis=1, inplace=True)

pd.set_option('display.max_colwidth', -1)
print(books.yearOfPublication.unique())

books.loc[books.ISBN == '0789466953', 'yearOfPublication'] = 2000
books.loc[books.ISBN == '0789466953', 'bookAuthor'] = 'James Buckley'
books.loc[books.ISBN == '0789466953', 'publisher'] = 'DK Publishing Inc'
books.loc[books.ISBN == '0789466953', 'bookTitle'] = 'DK Readers: Creating the X-Men, How Comic Books Come to Life (Level 4: Proficient Readers)'

books.loc[books.ISBN == '078946697X', 'yearOfPublication'] = 2000
books.loc[books.ISBN == '078946697X', 'bookAuthor'] = 'Michael Teitelbaum'
books.loc[books.ISBN == '078946697X', 'publisher'] = 'DK Publishing Inc'
books.loc[books.ISBN == '078946697X', 'bookTitle'] = 'DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient Readers)'

books.loc[books.ISBN == '2070426769', 'yearOfPublication'] = 2003
books.loc[books.ISBN == '2070426769', 'bookAuthor'] = 'Jean-Marie Gustave Le ClÃ?Â©zio'
books.loc[books.ISBN == '2070426769', 'publisher'] = 'Gallimard'
books.loc[books.ISBN == '2070426769', 'bookTitle'] = "Peuple du ciel, suivi de 'Les Bergers"

books.yearOfPublication = pd.to_numeric(books.yearOfPublication, errors='coerce')
print(sorted(books['yearOfPublication'].unique()))


books.loc[(books.yearOfPublication > 2006) | (books.yearOfPublication == 0), 'yearOfPublication'] = np.NAN
books.yearOfPublication.fillna(round(books.yearOfPublication.mean()), inplace=True)
books.yearOfPublication = books.yearOfPublication.astype(np.int32)

print(books.loc[books.publisher.isnull(), :])
books.loc[(books.ISBN == '193169656X'), 'publisher'] = 'other'
books.loc[(books.ISBN == '1931696993'), 'publisher'] = 'other'

users.loc[(users.Age > 90) | (users.Age < 5), 'Age'] = np.nan
users.Age = users.Age.fillna(users.Age.mean())
users.Age = users.Age.astype(np.int32)

n_users = users.shape[0]
n_books = books.shape[0]

ratings_new = ratings[ratings.ISBN.isin(books.ISBN)]
ratings_new = ratings_new[ratings_new.userID.isin(users.userID)]

print(ratings.shape)
print(ratings_new.shape)

print("number if users: "+str(n_users))
print("number if books: "+str(n_books))

sparsity = 1.0 - len(ratings_new) / float(n_users * n_books)
print('The sparsity level of Book Crossing dataset is ' + str(sparsity*100)+'%')

ratings_explicit = ratings_new[ratings_new.bookRating != 0]
ratings_implicit = ratings_new[ratings_new.bookRating == 0]

print(ratings_new.shape)
print(ratings_explicit.shape)
print(ratings_implicit.shape)

# sns.countplot(data=ratings_explicit, x='bookRating')
# plt.show()

ratings_count = pd.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
top10 = ratings_count.sort_values('bookRating', ascending=False).head(10)
print("Following books are recommended\n", top10.merge(books, left_index=True, right_on='ISBN'))


users_exp_ratings = users[users.userID.isin(ratings_explicit.userID)]
users_imp_ratings = users[users.userID.isin(ratings_implicit.userID)]

print(users.shape)
print(users_exp_ratings.shape)
print(users_imp_ratings.shape)

counts1 = ratings_explicit['userID'].value_counts()
ratings_explicit = ratings_explicit[ratings_explicit['userID'].isin(counts1[counts1 >= 100].index)]
counts = ratings_explicit['bookRating'].value_counts()
ratings_explicit = ratings_explicit[ratings_explicit['bookRating'].isin(counts[counts >= 100].index)]

ratings_matrix = ratings_explicit.pivot(index='userID', columns='ISBN', values='bookRating')
userID = ratings_matrix.index
ISBN = ratings_matrix.columns
print(ratings_matrix.shape)
print(ratings_matrix.head())

n_users = ratings_matrix.shape[0]
n_books = ratings_matrix.shape[1]
print(n_users, n_books)

ratings_matrix.fillna(0, inplace=True)
ratings_matrix = ratings_matrix.astype(np.int32)
print(ratings_matrix.head(5))

sparsity = 1.0-len(ratings_explicit)/float(users_exp_ratings.shape[0]*n_books)
print('The sparsity level of Book Crossing dataset is ' + str(sparsity*100) + ' %')

k = 10
metric = 'cosine'


def findksimilarusers(user_id, ratings, metric=metric, k=k):
    similarities = []
    indices = []
    model_knn = NearestNeighbors(metric=metric, algorithm='brute')
    model_knn.fit(ratings)
    loc = ratings.index.get_loc(user_id)
    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors=k + 1)
    similarities = 1 - distances.flatten()

    return similarities, indices


def predict_userbased(user_id, item_id, ratings, metric=metric, k=k):
    prediction = 0
    user_loc = ratings.index.get_loc(user_id)
    item_loc = ratings.columns.get_loc(item_id)
    similarities, indices = findksimilarusers(user_id, ratings, metric, k)  # similar users based on cosine similarity
    mean_rating = ratings.iloc[user_loc, :].mean()  # to adjust for zero based indexing
    sum_wt = np.sum(similarities) - 1
    product = 1
    wtd_sum = 0

    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == user_loc:
            continue;
        else:
            ratings_diff = ratings.iloc[indices.flatten()[i], item_loc] - np.mean(ratings.iloc[indices.flatten()[i], :])
            product = ratings_diff * (similarities[i])
            wtd_sum = wtd_sum + product

    # in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
    # which are handled here as below
    if prediction <= 0:
        prediction = 1
    elif prediction > 10:
        prediction = 10

    prediction = int(round(mean_rating + (wtd_sum / sum_wt)))
    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

    return prediction


# predict_userbased(11676, '0001056107', ratings_matrix)

def findksimilaritems(item_id, ratings, metric=metric, k=k):
    similarities = []
    indices = []
    ratings = ratings.T
    loc = ratings.index.get_loc(item_id)
    model_knn = NearestNeighbors(metric=metric, algorithm='brute')
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors=k + 1)
    similarities = 1 - distances.flatten()

    return similarities, indices


similarities, indices = findksimilaritems('0001056107',ratings_matrix)


def predict_itembased(user_id, item_id, ratings, metric=metric, k=k):
    prediction = wtd_sum = 0
    user_loc = ratings.index.get_loc(user_id)
    item_loc = ratings.columns.get_loc(item_id)
    similarities, indices = findksimilaritems(item_id, ratings)  # similar users based on correlation coefficients
    sum_wt = np.sum(similarities) - 1
    product = 1
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == item_loc:
            continue;
        else:
            product = ratings.iloc[user_loc, indices.flatten()[i]] * (similarities[i])
            wtd_sum = wtd_sum + product
    prediction = int(round(wtd_sum / sum_wt))

    # in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
    # which are handled here as below //code has been validated without the code snippet below, below snippet is to avoid negative
    # predictions which might arise in case of very sparse datasets when using correlation metric
    if prediction <= 0:
        prediction = 1
    elif prediction > 10:
        prediction = 10

    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

    return prediction


# prediction = predict_itembased(11676, '0001056107', ratings_matrix)


def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

'''
def recommendItem(user_id, ratings, metric=metric):
    if (user_id not in ratings.index.values) or type(user_id) is not int:
        print("User id should be a valid integer from this list :\n\n {} ".format(re.sub('[\[\]]', '', np.array_str(ratings_matrix.index.values))))
    else:
        ids = ['Item-based (correlation)','Item-based (cosine)','User-based (correlation)','User-based (cosine)']
        select = widgets.Dropdown(options=ids, value=ids[0],description='Select approach', width='1000px')
        def on_change(change):
            clear_output(wait=True)
            prediction = []
            if change['type'] == 'change' and change['name'] == 'value':
                if (select.value == 'Item-based (correlation)') | (select.value == 'User-based (correlation)') :
                    metric = 'correlation'
                else:
                    metric = 'cosine'
                with suppress_stdout():
                    if (select.value == 'Item-based (correlation)') | (select.value == 'Item-based (cosine)'):
                        for i in range(ratings.shape[1]):
                            if ratings[str(ratings.columns[i])][user_id] != 0:  # not rated already
                                prediction.append(predict_itembased(user_id, str(ratings.columns[i]) ,ratings, metric))
                            else:
                                prediction.append(-1)  # for already rated items
                    else:
                        for i in range(ratings.shape[1]):
                            if ratings[str(ratings.columns[i])][user_id] != 0:  # not rated already
                                prediction.append(predict_userbased(user_id, str(ratings.columns[i]) ,ratings, metric))
                            else:
                                prediction.append(-1)  # for already rated items
                prediction = pd.Series(prediction)
                prediction = prediction.sort_values(ascending=False)
                recommended = prediction[:10]
                print("As per {0} approach....Following books are recommended...".format(select.value))
                for i in range(len(recommended)):
                    print("{0}. {1}".format(i+1, books.bookTitle[recommended.index[i]].encode('utf-8')))
        select.observe(on_change)
        display(select)
'''

prediction = []
metric = 'cosine'
for i in range(ratings_matrix.shape[1]):
    if ratings_matrix[str(ratings_matrix.columns[i])][4385] != 0:
        prediction.append(predict_itembased(4385, str(ratings_matrix.columns[i]), ratings_matrix, metric))
    else:
        prediction.append(-1)

prediction = pd.Series(prediction)
prediction = prediction.sort_values(ascending=False)
recommended = prediction[:10]
print('As per itembased(cosine) approach....Following books are recommended...')
for i in range(len(recommended)):
    print("{0}. {1}".format(i+1, books.bookTitle[recommended.index[i]].encode('utf-8')))
