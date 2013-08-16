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



""" MERGE RATINGS WITH USERS """



""" MERGE ALL 3 TABLES IN ONE STEP """
#data = 



""" WHAT IS IN ROW 1345 ? """



""" HOW MANY PEOPLE REVIEWED THE MOVIE GOLDEN EYE ? (movie_id=10) """



"""" COMPARE THE MEAN RATINGS FOR MEN & WOMEN FOR EACH MOVIE """ 
#mean_ratings = 


""" SELECT ONLY MOVIES THAT RECEIVED AT LEAST 500 RATINGS """
#ratings_by_title = 
#active_titles = 



""" EXTRACT THESE MOVIES (the ones in active_titles) FROM mean_ratings """
#active_mean_ratings = 


""" WHAT ARE THE TOP 5 MOVIES AMONG MALE & FEMALE VIEWERS ? """
#top_f_ratings = 
#top_m_ratings = 


""" WHICH MOVIES HAVE THE HIGHEST DIFFERENCE IN RATINGS? """
#active_mean_ratings['diff'] = 
#sorted_by_diff = 



""" WHICH MOVIES HAVE THE SMALLEST DIFFERENCE IN RATINGS? """ 
#Reverse order of rows, take first 10 rows



""" APPLYMAP: FORMAT THE RATING TO HAVE 2 DECIMAL PLACES """
#formatted_f_ratings


""" FIND THE DIFFERENCE BETWEEN MALE & FEMALE RATINGS FOR EACH MOVIE 
    APPLY A CUSTOM FUNCTION TO EACH ROW OF top_f_ratings
"""
#movie_dif = 


