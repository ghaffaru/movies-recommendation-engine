import pandas as pd

from math import sqrt

import numpy as np

import matplotlib.pyplot as plt

movies_df = pd.read_csv('./data/movies.csv')

# print(movies_df.head())

movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)

movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)',expand=False)

movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')

movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())

# print(movies_df.head())

# Every genre is separated by a | so we simply have to call the split function on |

movies_df['genres'] = movies_df.genres.str.split('|')

# print(movies_df.head())

moviesWithGenre_df = movies_df.copy()

# one hot encoding of genres

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        moviesWithGenre_df.at[index, genre] = 1

# Filling in the NaN values with 0 to show that a movie doesn't have that column's genre

moviesWithGenres_df = moviesWithGenre_df.fillna(0)
print(moviesWithGenres_df.head())