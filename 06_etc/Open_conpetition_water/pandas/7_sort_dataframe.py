import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

# print(movies.title.sort_values())
# movie['title'].sort_values(ascending=False)

# print(movies.sort_values('duration', ascending=False))

print(movies.sort_values(['content_rating', 'duration']))
