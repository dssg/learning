# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from numpy.random import randn

# <codecell>

Series(randn(5)) 

# <codecell>

i = randn(5)
i_names = ['andrea', 'bob', 'evan', 'rob', 'kayla']
s=Series(i, i_names)

# <codecell>

s

# <codecell>

d={'a': 10, 'b': 20, 'c': 30}
Series(d)

# <codecell>

Series(d, index=['b', 'c', 'd', 'a'])

# <codecell>

s[1]

# <codecell>

s[:3]   

# <codecell>

s[s > s.median()]

# <codecell>

np.exp(s)

# <codecell>

s['evan']=9
s

# <codecell>

'bob' in s

# <codecell>

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data)
df

# <codecell>

df = DataFrame(data, columns=['state', 'year', 'pop'])
df

# <codecell>

df = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
df

# <codecell>

df['state']

# <codecell>

df.year

# <codecell>

df['debt'] = np.arange(5.)
df

# <codecell>

df.T

# <codecell>

'be retrieved by position or name by a couple of methods, such as the'
'ix indexing field'
df.ix[1,]

# <codecell>

df.ix[:1]

# <codecell>

df.ix[[0,2,4]]

# <codecell>

data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data

# <codecell>

data.index

# <codecell>

df1 = DataFrame({'key': ['a', 'b', 'c', 'd', 'e'], 
                 'data1': range(5)})
df2 = DataFrame({'key': ['a', 'd', 'f'], 
                 'data2': [1000, 2000, 3000]})
df1

# <codecell>

df2

# <codecell>

# merge
#    If not specified, merge uses the overlapping column names as the keys. 
#    It’s good practice to specify explicitly, though.'
pd.merge(df1, df2, on='key')

# <codecell>

pd.merge(df1, df2, how='inner')

# <codecell>

pd.merge(df1, df2, how='outer')

# <codecell>

# inner join: intersection
    
# outer join: union takes the union of the keys (combines the effect of applying both left and right joins)
    
# By default, merge does an 'inner' join

# <codecell>

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data)
df

# <codecell>

df.unstack()

# <codecell>

df.stack()

# <codecell>

df.pivot_table('pop', rows = 'year', aggfunc = 'mean')

# <codecell>

df.pivot_table('pop', rows = 'state', aggfunc = 'median')

# <codecell>

""" SET FILE PATH & FILE NAMES OF DATA FILES """
path = 'D:/DSSG/pandas_presentation/'
file1 = 'users.dat'
file2 = 'movies.dat'
file3 = 'ratings.dat'

# <codecell>

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

# <codecell>

# check 
ratings[:5]

# <codecell>

# check
users[:5]

# <codecell>

# check 
movies[:5]

# <codecell>

"""" GET MEAN & STD OF 'rating' IN THE ratings DATAFRAME """
ratings['rating'].describe()

# <codecell>

""" MERGE RATINGS WITH USERS """
d1 = pd.merge(ratings, users, on='user_id')
d1[:5]

# <codecell>

""" MERGE ALL 3 TABLES IN ONE STEP """
# merge ratings & users based on "user_id" key
# then merge the result with movies based on "movie_id" key
data = pd.merge(pd.merge(ratings, users, on='user_id'), movies, on='movie_id')

# <codecell>

# check 
data.columns

# <codecell>

#check 
data.values[:5]

# <codecell>

""" WHAT IS IN ROW 1345 ? """
data.ix[1345]  # or data.ix[1345,]

# <codecell>

""" HOW MANY PEOPLE REVIEWED THE MOVIE GOLDEN EYE ? (movie_id=10) """
len(data[data['movie_id']==10].values)

# <codecell>

"""" COMPARE THE MEAN RATINGS FOR MEN & WOMEN FOR EACH MOVIE """ 
mean_ratings = data.pivot_table('rating', rows='title',
                                cols='gender', aggfunc='mean')

# <codecell>

# check 
mean_ratings[:5]

# <codecell>

""" SELECT ONLY MOVIES THAT RECEIVED AT LEAST 500 RATINGS """
# group the data by title and use size() to get a Series 
# of group sizes for each title
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 500]

# <codecell>

# check 
active_titles[:10]
active_titles.size

# <codecell>

""" EXTRACT THESE MOVIES (the ones in active_titles) FROM mean_ratings """
active_mean_ratings = mean_ratings.ix[active_titles]
active_mean_ratings[:10]

# <codecell>

""" WHAT ARE THE TOP 5 MOVIES AMONG MALE & FEMALE VIEWERS ? """
#sort by the F column in descending order
top_f_ratings = active_mean_ratings.sort_index(by='F', ascending=False)
top_f_ratings[:5]
top_m_ratings = active_mean_ratings.sort_index(by='M', ascending=False)
top_m_ratings.index[:5]

# <codecell>

""" WHICH MOVIES HAVE THE HIGHEST DIFFERENCE IN RATINGS? """
active_mean_ratings['diff'] = active_mean_ratings['M'] - active_mean_ratings['F']
sorted_by_diff = active_mean_ratings.sort_index(by='diff')
sorted_by_diff[:10]

# <codecell>

""" WHICH MOVIES HAVE THE SMALLEST DIFFERENCE IN RATINGS? """ 
#Reverse order of rows, take first 10 rows
sorted_by_diff[::-1][:10]

# <codecell>

""" APPLYMAP: FORMAT THE RATING TO HAVE 2 DECIMAL PLACES """
format = lambda x: '%.2f' % x
formatted_f_ratings = top_f_ratings.applymap(format)
formatted_f_ratings[:10]

# <codecell>

""" FIND THE DIFFERENCE BETWEEN MALE & FEMALE RATINGS FOR EACH MOVIE 
    APPLY A CUSTOM FUNCTION TO EACH ROW OF top_f_ratings
"""
f = lambda x: x.max() - x.min()
top_f_ratings.apply(f)
movie_dif = top_f_ratings.apply(f, axis=1)  #axis=1 is 'columns'
movie_dif[:10]

