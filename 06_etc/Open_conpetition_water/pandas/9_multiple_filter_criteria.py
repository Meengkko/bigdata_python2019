import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')

# print(movies[movies.duration >= 200])

# print(movies[(movies.duration >= 200) and (movies.genre == 'Drama')])
# print(movies[(movies.duration >= 200) & (movies.genre == 'Drama')])  # and
# print(movies[(movies.duration >= 200) | (movies.genre == 'Drama')])  # or

# print(movies[movies.genre.isin(['Crime', 'Drama', 'Action'])])
print(movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')])

