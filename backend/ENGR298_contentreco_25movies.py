
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

data = pd.read_csv('C:\mm\movies.csv')


# In[3]:

#print movie-genre information
#print(data)


# In[4]:

#Step 1 - Generate movie-genre matrix
#df1: Columns - movieid, genres
#df1: Rows - movies

#Creating a new dataframe with columns
df1 = pd.DataFrame(columns=['ID','Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama',
                            'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western'])


# In[5]:

#df1.head()


# In[6]:

#Iterate over data and fill new datatframe
i = 1
for row in data.itertuples():
    #print(row)
    #print(row[1])
    df1.at[i, 'ID'] = row[1]
    str = row[2]
    parts = str.split('|')
    tot_genres = len(parts)
    for a in range(0,tot_genres):
        #print(parts[a])
        if(parts[a] == 'Adventure'):
            df1.at[i, 'Adventure'] = 1
        elif(parts[a] == 'Animation'):
            df1.at[i, 'Animation'] = 1
        elif(parts[a] == 'Action'):
            df1.at[i, 'Action'] = 1
        elif(parts[a] == 'Children'):
            df1.at[i, 'Children'] = 1 
        elif(parts[a] == 'Comedy'):
            df1.at[i, 'Comedy'] = 1 
        elif(parts[a] == 'Crime'):
            df1.at[i, 'Crime'] = 1
        elif(parts[a] == 'Documentary'):
            df1.at[i, 'Documentary'] = 1
        elif(parts[a] == 'Drama'):
            df1.at[i, 'Drama'] = 1 
        elif(parts[a] == 'Fantasy'):
            df1.at[i, 'Fantasy'] = 1 
        elif(parts[a] == 'Film-Noir'):
            df1.at[i, 'Film-Noir'] = 1
        elif(parts[a] == 'Horror'):
            df1.at[i, 'Horror'] = 1
        elif(parts[a] == 'Musical'):
            df1.at[i, 'Musical'] = 1 
        elif(parts[a] == 'Mystery'):
            df1.at[i, 'Mystery'] = 1 
        elif(parts[a] == 'Romance'):
            df1.at[i, 'Romance'] = 1 
        elif(parts[a] == 'Sci-Fi'):
            df1.at[i, 'Sci-Fi'] = 1
        elif(parts[a] == 'Thriller'):
            df1.at[i, 'Thriller'] = 1
        elif(parts[a] == 'War'):
            df1.at[i, 'War'] = 1 
        elif(parts[a] == 'Western'):
            df1.at[i, 'Western'] = 1 
    i=i+1

df1.fillna(0, inplace=True)

#Added on 15thFeb2018
#df1.set_index('ID')  

print(df1)


# In[8]:

#Step 2 - Generate user-rating matrix

data1 = pd.read_csv('C:\mm\\ratings_674.csv')


# In[9]:

#print rating information
#print(data1)


# In[10]:

#Total number of movies in ratings file. i.e. max(movieIDs)
#movieidmax = 10
movies_input = input('Enter total number of movies')
movieidmax = int(movies_input)

#Total number of users in ratings file. i.e. max(userID)
user_input = input('Enter number of users')
useridmax = int(user_input)

##Creating a new dataframe with columns
df2 = pd.DataFrame(index=range(0,useridmax))

#print(df2)


# In[11]:

#Iterate over data and fill new datatframe

i = 0
for row in data1.itertuples():
    userid = row[1]
    movieid = row[2]
    rating = row[3]
    if(rating >=3):
        bin_rating = 1
    elif(rating <3):
        bin_rating = -1
    else:
        bin_rating = 0
    if(row[0] == 0):
        df2.at[i,0] = userid
        df2.at[i,movieid] = bin_rating
    else:
        prev_userid = df2.at[i,0]
        if(prev_userid == userid):
            df2.at[i,movieid] = bin_rating
        else:
            i=i+1
            df2.at[i,0] = userid
            df2.at[i,movieid] = bin_rating
            

df2.fillna(0, inplace=True)
df2[0] = df2[0].astype(int)
#df2.set_index(0)

print(df2)


# In[12]:

#Added on 15th Feb 2018 
#Testing Pending

#pd.DataFrame(data=data1[1:,1:],index=data[1:,0],columns=data[0,1:])


# In[13]:

#Added on 15th Feb 2018 

#Get the number of columns in df2, i.e. no of movies rated by all users

tot_rated_movies = df2.shape[1] - 1
print('No of total movies rated by users = ' + repr(tot_rated_movies))

#Sort columns in ascending order of movies
df2.reindex_axis(sorted(df2.columns), axis=1)

#Get number of rows in df1, i.e. total # of movies
tot_movies = df1.shape[0]
print('Total no of movies in dataset = ' + repr(tot_movies))
#Don't have to sort, as these are already in sorted order from file

#Generate list with all column headers in df2. i.e., sorted list of all movies rated
rated_movies_list = list(df2)
rated_movies_list.pop(0)
rated_movies_list.sort()
print('List of movies rated')
print(rated_movies_list)


dataset_movies_list = list(df1['ID'])
print('List of all movies')
print(dataset_movies_list)

#comparing number of movies in dataset and in ratings file
if(len(rated_movies_list) != len(dataset_movies_list)):
    df2_new = pd.DataFrame(index=range(0,useridmax))

#copy columns from df2 to df2_new if it exists in df2. Else insert an empty column (all 0s) in that position in df2_new.
for i in range(0,tot_movies):
    print('i = ' + repr(i))
    dataset_movie_id = dataset_movies_list[i]
    dataset_movie_index = i
    print('dataset_movie_id = ' + repr(dataset_movie_id))
    if (i<tot_rated_movies):
        rated_movie_id = rated_movies_list[i]
        print('rated_movie_id = ' + repr(rated_movie_id))
        if(rated_movie_id != dataset_movie_id):
            print('Dont match')
            print('Insert new column')
            df2_new.insert(i, dataset_movie_id, 0)
            rated_movies_list.insert(i, dataset_movie_id)
            tot_rated_movies = tot_rated_movies + 1
            print('Updated rated_movies_list:')
            #print(rated_movies_list)
        else:
            print('copy column from df2 to df2_new')
            df2_new.insert(i, dataset_movie_id, df2[dataset_movie_id])
    else:
        print('insert column at end')
        df2_new.insert(i, dataset_movie_id, 0)
    print('********************\n')

#print(df2_new)
df2_new.insert(0, 0, df2[0])

print(df2_new)


# In[14]:

#Step 3 - Creating user profiles

#To enable dot product, creating new dataframe df3 from df2, by removing only the first column, i.e. the userid column
#This makes no of columns of df2 = no of rows in df1, thus enabling a dot product

df3 = df2_new.drop(0, axis=1)
df3.apply(pd.to_numeric)
#print('Binary user-movie rating matrix')
#print(df3)
#print('***********************************\n')
#Also, removing the movieid column(1st column) from the movie x genre matrix, i.e. df1, and creating a new dataframe df4

df4 = df1.drop('ID', axis=1)
#print('Movie-genre matrix')
#print(df4)
#print('***********************************\n')

#print('shape of df2 = ' + repr(np.shape(df2)))
#print('shape of df3 = ' + repr(np.shape(df3)))
#print('After dropping the first column')
#print('shape of df1 = ' + repr(np.shape(df1)))
#print('shape of df4 = ' + repr(np.shape(df4)))
#print('***********************************\n')



# In[15]:

#Creating a dot product of the dataframes df3 and df4
df5 = df2_new.set_index(0).dot(df1.set_index('ID'))
#data_1 = np.dot(df3, df4)
#print('User profiles matrix')
print(df5)


# In[16]:

#To calculate score for each unwatched movie, iterate through each row of df3

#df_content_reco = pd.DataFrame(columns=['movieid1','movieid2','movieid3'])
df_content_reco = pd.DataFrame(columns=['movieid1','movieid2','movieid3','movieid4','movieid5','movieid6','movieid7','movieid8',
                                        'movieid9','movieid10','movieid11','movieid12','movieid13','movieid14','movieid15',
                                        'movieid16','movieid17','movieid18','movieid19','movieid20','movieid21','movieid22',
                                        'movieid23','movieid24','movieid25'])

i=0

for row in df3.itertuples():
    rownumn = i
    userid = df2_new.at[i,0]
    if(userid != 0):
        print('userid = ' + repr(userid))
        df6 = pd.DataFrame()
        df6 = df5.iloc[i,:] #User-Profile
        #print(df6)
        #cols = tot_movies + 1
        #Create a temp dataframe to hold all movieids and corresponding values
        #for movies not rated by a user
        df_temp = pd.DataFrame(columns=['movieid','value']) #dataframe to hold movies and their scores
        j=1
        for column in df3: #iterate through each column and check for rating
            movieid = column
            rating = row[j]
            #print(rating)
            # check if movie is not rated by user
            if(rating == 0): #compute score for movies not rated by the user
                df7 = df4.iloc[j-1,:] #the movie's genre profile
                df8 = df7.transpose() #to enable dot product with df6
                df9 = df6.dot(df8) #scalar value = score for the movie
                pd.to_numeric(df9)
                rating_value = df9
                df_temp = df_temp.append({'movieid': movieid,'value': rating_value},ignore_index=True)
            j=j+1
        #print('Top 3 movies')
        #print(df_temp.sort_values('value', ascending=False).head(3)[['movieid', 'value']])
        df_content_reco_temp1 = df_temp.sort_values('value', ascending=False).head(25)['movieid']
        df_content_reco_temp1 = df_content_reco_temp1.reset_index(drop=True)
        movie_1 = df_content_reco_temp1.at[0]
        movie_2 = df_content_reco_temp1.at[1]
        movie_3 = df_content_reco_temp1.at[2]
        movie_4 = df_content_reco_temp1.at[3]
        movie_5 = df_content_reco_temp1.at[4]
        movie_6 = df_content_reco_temp1.at[5]
        movie_7 = df_content_reco_temp1.at[6]
        movie_8 = df_content_reco_temp1.at[7]
        movie_9 = df_content_reco_temp1.at[8]
        movie_10 = df_content_reco_temp1.at[9]
        movie_11 = df_content_reco_temp1.at[10]
        movie_12 = df_content_reco_temp1.at[11]
        movie_13 = df_content_reco_temp1.at[12]
        movie_14 = df_content_reco_temp1.at[13]
        movie_15 = df_content_reco_temp1.at[14]
        movie_16 = df_content_reco_temp1.at[15]
        movie_17 = df_content_reco_temp1.at[16]
        movie_18 = df_content_reco_temp1.at[17]
        movie_19 = df_content_reco_temp1.at[18]
        movie_20 = df_content_reco_temp1.at[19]
        movie_21 = df_content_reco_temp1.at[20]
        movie_22 = df_content_reco_temp1.at[21]
        movie_23 = df_content_reco_temp1.at[22]
        movie_24 = df_content_reco_temp1.at[23]
        movie_25 = df_content_reco_temp1.at[24]
        df_content_reco.at[i,'movieid1'] = movie_1
        df_content_reco.at[i,'movieid2'] = movie_2
        df_content_reco.at[i,'movieid3'] = movie_3
        df_content_reco.at[i,'movieid4'] = movie_4
        df_content_reco.at[i,'movieid5'] = movie_5
        df_content_reco.at[i,'movieid6'] = movie_6
        df_content_reco.at[i,'movieid7'] = movie_7
        df_content_reco.at[i,'movieid8'] = movie_8
        df_content_reco.at[i,'movieid9'] = movie_9
        df_content_reco.at[i,'movieid10'] = movie_10
        df_content_reco.at[i,'movieid11'] = movie_11
        df_content_reco.at[i,'movieid12'] = movie_12
        df_content_reco.at[i,'movieid13'] = movie_13
        df_content_reco.at[i,'movieid14'] = movie_14
        df_content_reco.at[i,'movieid15'] = movie_15
        df_content_reco.at[i,'movieid16'] = movie_16
        df_content_reco.at[i,'movieid17'] = movie_17
        df_content_reco.at[i,'movieid18'] = movie_18
        df_content_reco.at[i,'movieid19'] = movie_19
        df_content_reco.at[i,'movieid20'] = movie_20
        df_content_reco.at[i,'movieid21'] = movie_21
        df_content_reco.at[i,'movieid22'] = movie_22
        df_content_reco.at[i,'movieid23'] = movie_23
        df_content_reco.at[i,'movieid24'] = movie_24
        df_content_reco.at[i,'movieid25'] = movie_25
        #print('********* df_content_reco *************')
        #print(df_content_reco)
        #print('**************************************************************\n\n')
        i=i+1

#print('********* df_user_content_reco *************')
#print(df_content_reco)
df_content_reco = df_content_reco.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df_user_content_reco = pd.concat([df_content_reco, df2[0]], axis=1)
new_cols = ['movieid1','movieid2','movieid3','movieid4','movieid5','movieid6','movieid7','movieid8','movieid9','movieid10',
            'movieid11','movieid12','movieid13','movieid14','movieid15','movieid16','movieid17','movieid18','movieid19',
            'movieid20','movieid21','movieid22','movieid23','movieid24','movieid25','userid']
df_user_content_reco.columns = new_cols
#print(df_user_content_reco)


# In[17]:

#Connect to database and insert into table
#Import dataframe into MySQL

import sqlalchemy
from sqlalchemy import create_engine
import pymysql

#Heroku DB Details

database_username = 'ba0dd49e70befd'
database_password = 'e8e0885d'
database_ip       = 'us-cdbr-iron-east-05.cleardb.net'
database_name     = 'heroku_54c3b520208a1ef'
database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,database_ip, database_name))

#GoDaddy DB Details

#database_username = 'movie_db_user1'
#database_password = '12345'
#type(database_password)
#database_ip       = '//107.180.48.201/movie_recommendation_db'
#database_name     = 'mysql'
#database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
 #                                              format(database_username, database_password,database_ip, database_name))


# In[18]:

a = 5
type(a)


# In[19]:

df_user_content_reco.dtypes


# In[20]:

pd.set_option('precision', 0)


# In[21]:

df_user_content_reco['movieid1'] = df_user_content_reco['movieid1'].astype('str')
df_user_content_reco['movieid2'] = df_user_content_reco['movieid2'].astype('str')
df_user_content_reco['movieid3'] = df_user_content_reco['movieid3'].astype('str')
df_user_content_reco['movieid4'] = df_user_content_reco['movieid4'].astype('str')
df_user_content_reco['movieid5'] = df_user_content_reco['movieid5'].astype('str')
df_user_content_reco['movieid6'] = df_user_content_reco['movieid6'].astype('str')
df_user_content_reco['movieid7'] = df_user_content_reco['movieid7'].astype('str')
df_user_content_reco['movieid8'] = df_user_content_reco['movieid8'].astype('str')
df_user_content_reco['movieid9'] = df_user_content_reco['movieid9'].astype('str')
df_user_content_reco['movieid10'] = df_user_content_reco['movieid10'].astype('str')
df_user_content_reco['movieid11'] = df_user_content_reco['movieid11'].astype('str')
df_user_content_reco['movieid12'] = df_user_content_reco['movieid12'].astype('str')
df_user_content_reco['movieid13'] = df_user_content_reco['movieid13'].astype('str')
df_user_content_reco['movieid14'] = df_user_content_reco['movieid14'].astype('str')
df_user_content_reco['movieid15'] = df_user_content_reco['movieid15'].astype('str')
df_user_content_reco['movieid16'] = df_user_content_reco['movieid16'].astype('str')
df_user_content_reco['movieid17'] = df_user_content_reco['movieid17'].astype('str')
df_user_content_reco['movieid18'] = df_user_content_reco['movieid18'].astype('str')
df_user_content_reco['movieid19'] = df_user_content_reco['movieid19'].astype('str')
df_user_content_reco['movieid20'] = df_user_content_reco['movieid20'].astype('str')
df_user_content_reco['movieid21'] = df_user_content_reco['movieid21'].astype('str')
df_user_content_reco['movieid22'] = df_user_content_reco['movieid22'].astype('str')
df_user_content_reco['movieid23'] = df_user_content_reco['movieid23'].astype('str')
df_user_content_reco['movieid24'] = df_user_content_reco['movieid24'].astype('str')
df_user_content_reco['movieid25'] = df_user_content_reco['movieid25'].astype('str')


# In[22]:

df_user_content_reco.to_sql(con=database_connection, name='content_reco', if_exists='replace',flavor='mysql')


# In[ ]:



