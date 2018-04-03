
# coding: utf-8

# In[24]:

import numpy as np
import pandas as pd


# In[25]:

#Read the movies file and store all the movies in a dataframe

movies_data = pd.read_csv('C:\mm\movies.csv')

df_all_movies = pd.DataFrame()

i=0
for row in movies_data.itertuples():
    movieid = row[1]
    df_all_movies.at[i,0] = movieid
    i = i + 1

#print(df_all_movies)


# In[28]:

#Read rating file and generate binary rating user x movie matrix
#Rated movies will be 1 and non-rated movies will be 0

rating_data = pd.read_csv('C:\mm\cooccurence\\ratings_100K\\ratings.csv')

#Creating a new dataframe to hold the binary rating matrix
df_binary_rating = pd.DataFrame()

i = 0
for row in rating_data.itertuples():
    userid = row[1]
    movieid = row[2]
    if(row[0] == 0):
        df_binary_rating.at[i,0] = userid
        df_binary_rating.at[i,movieid] = 1
    else:
        prev_userid = df_binary_rating.at[i,0]
        if(prev_userid == userid):
            df_binary_rating.at[i,movieid] = 1
        else:
            i=i+1
            df_binary_rating.at[i,0] = userid
            df_binary_rating.at[i,movieid] = 1
            

df_binary_rating.fillna(0, inplace=True)
df_binary_rating[0] = df_binary_rating[0].astype(int)
df_binary_rating.set_index(0)
cols = df_binary_rating.columns[df_binary_rating.dtypes.eq('object')]
df_binary_rating[cols] = df_binary_rating[cols].apply(pd.to_numeric, errors='coerce')

print('User Binary Rating Matrix\n')
print(df_binary_rating)


# In[27]:

#Iterate through the binary ratings dataframe.
#For each user(row), create a new dataframe df_rated and store list of all movies rated by the user
#Create a new dataframe to store the difference between these two lists, i.e. list of movies not rated by the user
#Pick 50 movies from these at random and store to another dataframe

#Dataframe to store 50 unrated movies for all users
df_not_rated_all = pd.DataFrame()

i=0
for row in df_binary_rating.itertuples():
    userid = row[1]
    df_rated = pd.DataFrame()
    df_not_rated = pd.DataFrame()
    if (userid != 0):
        j=0
        for column in df_binary_rating:
            if(column != 0):
                #print('Movie ID = ' + repr(column))
                if(df_binary_rating.at[i,column] == 1):
                    df_rated.at[j,0] = column
                    j=j+1
        print('userid = ' + repr(userid))
        #print(df_rated)
        df_all_movies.columns = ['movieid']
        df_rated.columns = ['movieid']
        df_all_movies['movieid'] = df_all_movies['movieid'].astype(float)
        df_all_movies['movieid'] = df_all_movies['movieid'].astype(int)
        df_all_movies = df_all_movies.reset_index(drop=True)
        df_rated['movieid'] = df_rated['movieid'].astype(float)
        df_rated['movieid'] = df_rated['movieid'].astype(int)
        df_rated = df_rated.reset_index(drop=True)
        ds1 = set([ tuple(line) for line in df_all_movies.values.tolist()])
        ds2 = set([ tuple(line) for line in df_rated.values.tolist()])
        df_not_rated = pd.DataFrame(list(ds1.difference(ds2)))
        df_not_rated.columns = ['movieid']
        df_not_rated = df_not_rated.sort_values('movieid', ascending=True)
        df_not_rated = df_not_rated.reset_index(drop=True)
        #Pick 5 movies at random from the list of movies not rated by the user
        df_random = df_not_rated.sample(n=50)
        df_random.columns = ['movieid']
        df_random = df_random.reset_index(drop=True)
        #print(df_random)
        df_not_rated_all.at[i,'UserID'] = userid
        for k in range(0,50):
            df_not_rated_all.loc[i,k] = df_random.at[k,'movieid']
        #print('******************************') 
    i=i+1

#df_not_rated_all = pd.DataFrame(columns=['UserID','movieid1','movieid2','movieid3','movieid4','movieid5'])
print('df_not_rated_all')
print(df_not_rated_all)
    
        



# In[30]:

#df_not_rated_all.columns = ['UserID','movieid1','movieid2','movieid3','movieid4','movieid5']
df_not_rated_all.columns = ['UserID','movieid1','movieid2','movieid3','movieid4','movieid5','movieid6','movieid7',
                                         'movieid8','movieid9','movieid10','movieid11','movieid12','movieid13','movieid14',
                                         'movieid15','movieid16','movieid17','movieid18','movieid19','movieid20','movieid21',
                                         'movieid22','movieid23','movieid24','movieid25','movieid26','movieid27','movieid28',
                                         'movieid29','movieid30','movieid31','movieid32','movieid33','movieid34','movieid35',
                                         'movieid36','movieid37','movieid38','movieid39','movieid40','movieid41','movieid42',
                                         'movieid43','movieid44','movieid45','movieid46','movieid47','movieid48','movieid49',
                                         'movieid50']

#print(df_not_rated_all)


# In[31]:

#Connect to database and insert into table
#Import dataframe into MySQL

import sqlalchemy
from sqlalchemy import create_engine
import pymysql

database_username = 'ba0dd49e70befd'
database_password = 'e8e0885d'
database_ip       = 'us-cdbr-iron-east-05.cleardb.net'
database_name     = 'heroku_54c3b520208a1ef'
database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,database_ip, database_name))


# In[32]:

df_not_rated_all.to_sql(con=database_connection, name='not_rated_reco', if_exists='replace',flavor='mysql')


# In[ ]:



