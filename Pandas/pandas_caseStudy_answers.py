import numpy as np
import pandas as pd
from pandas import DataFrame, Series

""" 
    Download "movieLens 1M" data set from "http://www.grouplens.org/node/73"
    - contains 1 million ratings collected from 6000 users on 4000 movies
    - data spread across 3 tables: ratings, user information, movie info
"""


""" SET FILE PATH & FILE NAMES OF DATA FILES """
path = 'D:/DSSG/pandas_presentation/'
file1 = 'users.dat'
file2 = 'movies.dat'
file3 = 'ratings.dat'


""" LOAD EACH TABLE INTO A PANDAS DATAFRAME OBJECT """
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path + file1, 
                      sep='::', header=None,names=unames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(path + file2, sep='::', header=None,
                       names=mnames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(path + file3, sep='::', header=None,
                        names=rnames)

# check 
ratings[:5]
users[:5]
movies[:5]


"""" GET MEAN & STD OF 'rating' IN THE ratings DATAFRAME """
ratings['rating'].describe()

""" MERGE RATINGS WITH USERS """
d1 = pd.merge(ratings, users, on='user_id')
d1[:5]
# d1 = pd.merge(ratings, users) also works because
# pandas infers which columns to use as the merge (or join) keys
# based on the names that are common to both data tables


""" MERGE ALL 3 TABLES IN ONE STEP """
# merge ratings & users based on "user_id" key
# then merge the result with movies based on "movie_id" key
data = pd.merge(pd.merge(ratings, users, on='user_id'), movies, on='movie_id')
# check 
data.columns
data.values[:5]


""" WHAT IS IN ROW 1345 ? """
data.ix[1345]
data.ix[1345,]


""" HOW MANY PEOPLE REVIEWED THE MOVIE GOLDEN EYE ? (movie_id=10) """
len(data[data['movie_id']==10].values)


"""" COMPARE THE MEAN RATINGS FOR MEN & WOMEN FOR EACH MOVIE """ 
mean_ratings = data.pivot_table('rating', rows='title',
                                cols='gender', aggfunc='mean')
# check 
mean_ratings[:5]

'two pivot table examples

""" SELECT ONLY MOVIES THAT RECEIVED AT LEAST 500 RATINGS """
# group the data by title and use size() to get a Series 
# of group sizes for each title
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 500]
# check 
active_titles[:10]
active_titles.size


""" EXTRACT THESE MOVIES (the ones in active_titles) FROM mean_ratings """
active_mean_ratings = mean_ratings.ix[active_titles]
active_mean_ratings[:10]


""" WHAT ARE THE TOP 5 MOVIES AMONG MALE & FEMALE VIEWERS ? """
#sort by the F column in descending order
top_f_ratings = active_mean_ratings.sort_index(by='F', ascending=False)
top_f_ratings[:5]
top_m_ratings = active_mean_ratings.sort_index(by='M', ascending=False)
top_m_ratings.index[:5]


""" WHICH MOVIES HAVE THE HIGHEST DIFFERENCE IN RATINGS? """
active_mean_ratings['diff'] = active_mean_ratings['M'] - active_mean_ratings['F']
sorted_by_diff = active_mean_ratings.sort_index(by='diff')
sorted_by_diff[:10]


""" WHICH MOVIES HAVE THE SMALLEST DIFFERENCE IN RATINGS? """ 
#Reverse order of rows, take first 10 rows
sorted_by_diff[::-1][:10]


""" APPLYMAP: FORMAT THE RATING TO HAVE 2 DECIMAL PLACES """
format = lambda x: '%.2f' % x
formatted_f_ratings = top_f_ratings.applymap(format)
formatted_f_ratings[:10]


""" FIND THE DIFFERENCE BETWEEN MALE & FEMALE RATINGS FOR EACH MOVIE 
    APPLY A CUSTOM FUNCTION TO EACH ROW OF top_f_ratings
"""
f = lambda x: x.max() - x.min()
top_f_ratings.apply(f)
movie_dif = top_f_ratings.apply(f, axis=1)  #axis=1 is 'columns'
movie_dif[:10]



