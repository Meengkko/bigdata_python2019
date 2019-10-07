import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
booleans = []

'''
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

is_long = pd.Series(booleans)
print(is_long.head())
'''

is_long = movies.duration >= 200
print(is_long.head())

# movies[movies.duration >= 200]
# movies[is_long].genre

print(movies.loc[movies.duration >= 200, 'genre'])


