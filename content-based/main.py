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

print(movies_df.head())