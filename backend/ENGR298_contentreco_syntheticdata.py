
# coding: utf-8

# In[13]:

import numpy as np
import pandas as pd


# In[14]:

#User-input userid
input_1 = input('Enter the user ID')
input_userid = int(input_1)


# In[15]:

#User-input new/existing user
input_6 = input('New(N)/Existing(E) User?')
input_user = input_6


# In[16]:

#User-input three genres
input_3 = input('Enter genre 1 , 1.Action ,2.Adventure, 3.Animation, 4.Children, 5.Comedy, 6.Crime, 7.Documentary, 8.Drama, 9.Fantasy, 10.Film-Noir, 11.Horror, 12.Musical, 13.Mystery, 14.Romance, 15.Sci-Fi, 16.Thriller, 17.War, 18.Western')
input_genre1 = int(input_3)

input_4 = input('Enter genre 2 ')
input_genre2 = int(input_4)

input_5 = input('Enter genre 3 ')
input_genre3 = int(input_5)


# In[17]:

#User-input number of movies whose ratings are to be added
input_2 = input('Enter the number of movies (minimum 15)')
input_count_movies = int(input_2)


# In[18]:

#Additional processing for existing users

if(input_user == 'E'):
    #Read the complete ratings file
    data_ratings = pd.read_csv(r'C:\mm\ratings.csv')
    #Create a list to hold all movies rated by the user
    list_rated = []
    
#If existing user, read the latest ratings file and remove those movies from the lists
if(input_user == 'E'):
    #Read each movie rated by user and append to list_rated
    for row in data_ratings.itertuples():
        userid = row[1]
        movieid = row[2]
        if(userid == input_userid):
            list_rated.append(movieid)
    list_rated.sort()
    print(list_rated)


# In[19]:

#Read the complete movies file
data = pd.read_csv('C:\mm\movies.csv')


# In[20]:

#Step 1 - Generate movie-genre matrix
#df1: Columns - movieid, genres
#df1: Rows - movies

#New columns - Total - total number of genres
#New columns - Chosen - total number of genres present from the user's input

#Creating a new dataframe with columns
df1 = pd.DataFrame(columns=['ID','Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama',
                            'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','Total','Chosen'])


# In[21]:

#df1.head()


# In[29]:

#Iterate over data and fill new datatframe
i = 1
for row in data.itertuples():
    #print(row)
    #print(row[1])
    total = 0
    chosen = 0
    others = 0
    movieid = row[1]
    if(input_user == 'E' and movieid in list_rated):
        #print('movie id already rated = ' + repr(movieid))
        continue
    df1.at[i, 'ID'] = row[1] #movieID in file
    str = row[2] #All genres of the movie 
    parts = str.split('|') #Splitting to get individual genres
    tot_genres = len(parts) 
    for a in range(0,tot_genres):
        #print(parts[a])
        if(parts[a] == 'Adventure'):
            df1.at[i, 'Adventure'] = 1
            total = total + 1 #if genre present, add to Total
            if((input_genre1 == 1) or (input_genre2 == 1) or(input_genre3 == 1)): #if genre is input, add to Chosen
                chosen = chosen + 1
        elif(parts[a] == 'Animation'):
            df1.at[i, 'Animation'] = 1
            total = total + 1
            if((input_genre1 == 2) or (input_genre2 == 2) or(input_genre3 == 2)):
                chosen = chosen + 1
        elif(parts[a] == 'Action'):
            df1.at[i, 'Action'] = 1
            total = total + 1
            if((input_genre1 == 3) or (input_genre2 == 3) or(input_genre3 == 3)):
                chosen = chosen + 1
        elif(parts[a] == 'Children'):
            df1.at[i, 'Children'] = 1
            total = total + 1
            if((input_genre1 == 4) or (input_genre2 == 4) or(input_genre3 == 4)):
                chosen = chosen + 1
        elif(parts[a] == 'Comedy'):
            df1.at[i, 'Comedy'] = 1 
            total = total + 1
            if((input_genre1 == 5) or (input_genre2 == 5) or(input_genre3 == 5)):
                chosen = chosen + 1
        elif(parts[a] == 'Crime'):
            df1.at[i, 'Crime'] = 1
            total = total + 1
            if((input_genre1 == 6) or (input_genre2 == 6) or(input_genre3 == 6)):
                chosen = chosen + 1
        elif(parts[a] == 'Documentary'):
            df1.at[i, 'Documentary'] = 1
            total = total + 1
            if((input_genre1 == 7) or (input_genre2 == 7) or(input_genre3 == 7)):
                chosen = chosen + 1
        elif(parts[a] == 'Drama'):
            df1.at[i, 'Drama'] = 1
            total = total + 1
            if((input_genre1 == 8) or (input_genre2 == 8) or(input_genre3 == 8)):
                chosen = chosen + 1
        elif(parts[a] == 'Fantasy'):
            df1.at[i, 'Fantasy'] = 1 
            total = total + 1
            if((input_genre1 == 9) or (input_genre2 == 9) or(input_genre3 == 9)):
                chosen = chosen + 1
        elif(parts[a] == 'Film-Noir'):
            df1.at[i, 'Film-Noir'] = 1
            total = total + 1
            if((input_genre1 == 10) or (input_genre2 == 10) or(input_genre3 == 10)):
                chosen = chosen + 1
        elif(parts[a] == 'Horror'):
            df1.at[i, 'Horror'] = 1
            total = total + 1
            if((input_genre1 == 11) or (input_genre2 == 11) or(input_genre3 == 11)):
                chosen = chosen + 1
        elif(parts[a] == 'Musical'):
            df1.at[i, 'Musical'] = 1 
            total = total + 1
            if((input_genre1 == 12) or (input_genre2 == 12) or(input_genre3 == 12)):
                chosen = chosen + 1
        elif(parts[a] == 'Mystery'):
            df1.at[i, 'Mystery'] = 1 
            total = total + 1
            if((input_genre1 == 13) or (input_genre2 == 13) or(input_genre3 == 13)):
                chosen = chosen + 1
        elif(parts[a] == 'Romance'):
            df1.at[i, 'Romance'] = 1 
            total = total + 1
            if((input_genre1 == 14) or (input_genre2 == 14) or(input_genre3 == 14)):
                chosen = chosen + 1
        elif(parts[a] == 'Sci-Fi'):
            df1.at[i, 'Sci-Fi'] = 1
            total = total + 1
            if((input_genre1 == 15) or (input_genre2 == 15) or(input_genre3 == 15)):
                chosen = chosen + 1
        elif(parts[a] == 'Thriller'):
            df1.at[i, 'Thriller'] = 1
            total = total + 1
            if((input_genre1 == 16) or (input_genre2 == 16) or(input_genre3 == 16)):
                chosen = chosen + 1
        elif(parts[a] == 'War'):
            df1.at[i, 'War'] = 1 
            total = total + 1
            if((input_genre1 == 17) or (input_genre2 == 17) or(input_genre3 == 17)):
                chosen = chosen + 1
        elif(parts[a] == 'Western'):
            df1.at[i, 'Western'] = 1 
            total = total + 1
            if((input_genre1 == 18) or (input_genre2 == 18) or(input_genre3 == 18)):
                chosen = chosen + 1
    df1.at[i, 'Total'] = total
    df1.at[i, 'Chosen'] = chosen
    i=i+1

df1.fillna(0, inplace=True)

#Added on 15thFeb2018
#df1.set_index('ID')  

#print(df1)


# In[30]:

#Create lists to store movies with different genre combinations
#Since movies with higher ratio of genres chosen : genres total should be rated higher, we create different lists

list1 = [] # Total-3; Chosen-3
list2 = [] # Total-2; Chosen-2
list3 = [] # Total-1; Chosen-1
list4 = [] # Total-3; Chosen-2
list5 = [] # Total-2; Chosen-1
list6 = [] # Total-3; Chosen-1
list7 = [] # Total>3; Chosen-3
list8 = [] # Total>3; Chosen-2
list9 = [] # Total>3; Chosen-1

 


# In[31]:

#Iterate through df1 and populate all lists based on 'Total' and 'Chosen' values

for row in df1.itertuples():
    movieid = row[1]
    total = row[20]
    chosen = row[21]
    if((total == 3) and (chosen == 3)):
        list1.append(movieid)
    elif((total == 2) and (chosen == 2)):
        list2.append(movieid)
    elif((total == 1) and (chosen == 1)):
        list3.append(movieid)
    elif((total == 3) and (chosen == 2)):
        list4.append(movieid)
    elif((total == 2) and (chosen == 1)):
        list5.append(movieid)    
    elif((total == 3) and (chosen == 1)):
        list6.append(movieid)
    elif((total > 3) and (chosen == 3)):
        list7.append(movieid)
    elif((total > 3) and (chosen == 2)):
        list8.append(movieid)
    elif((total > 3) and (chosen == 1)):
        list9.append(movieid)



# In[32]:

import random

#Shuffle all lists seperately to ensure a good mix of movies, instead of always picking movies from the beginning

list1_len = len(list1)
random.shuffle(list1)

list2_len = len(list2)
random.shuffle(list2)

list3_len = len(list3)
random.shuffle(list3)

list4_len = len(list4)
random.shuffle(list4)

list5_len = len(list5)
random.shuffle(list5)

list6_len = len(list6)
random.shuffle(list6)

list7_len = len(list7)
random.shuffle(list7)

list8_len = len(list8)
random.shuffle(list8)

list9_len = len(list9)
random.shuffle(list9)

tot_movies = list1_len + list2_len + list3_len + list4_len  + list5_len + list6_len + list7_len + list8_len + list9_len
print('Total movies = ' + repr(tot_movies))

print(df1.shape)


# In[33]:

#Building the recommndations from the lists

#list to hold the final recommendations
reco_list = []

#Check if we have enough movies in the selected genres to recommend
if((list1_len + list2_len + list3_len) >= input_count_movies):
    other_genre = 0
else:
    other_genre = input_count_movies - (list1_len + list2_len + list3_len)
#Fill reco_list from list1, list 2 and list3 if these have enough movies
if(other_genre == 0):
    for i in range(1,input_count_movies+1):
        if(other_genre == 0):
            if(i%3 == 1):
                movieid = list1.pop()
                reco_list.append(movieid)
            elif(i%3 == 2):
                movieid = list2.pop()
                reco_list.append(movieid)
            elif(i%3 == 0):
                movieid = list3.pop()
                reco_list.append(movieid)  
else:
        reco_list.extend(list1) #Add list1, list2 and list3 to final list
        reco_list.extend(list2)
        reco_list.extend(list3)
        for i in range(1,other_genre+1): #For the rest of the final list, pick movies from lists 4,5,7 and 8
            if(i%4 == 1):
                movieid = list4.pop()
                reco_list.append(movieid)
            elif(i%4 == 2):
                movieid = list5.pop()
                reco_list.append(movieid)
            elif(i%4 == 3):
                movieid = list7.pop()
                reco_list.append(movieid)
            elif(i%4 == 0):
                movieid = list8.pop()
                reco_list.append(movieid)

print('length of reco_list = ' + repr(len(reco_list)))
print(reco_list)


# In[35]:

#From final list, generate data in the format to be entered into the file
from datetime import datetime
timestamp = datetime.now().strftime('%Y%m%d')

text = ''
i=0

#text = text + repr(input_userid)
#print(text)

while(i < len(reco_list)):
    text = text + repr(input_userid) + ',' + repr(reco_list[i])  + ',' + repr(i%3 + 3) + ',' + timestamp + '\n'
    i=i+1

print(text)


# In[36]:

import os

#Write data from string into csv file

filename = 'ratings_' + repr(input_userid) +'.csv'
print(filename)

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

with open(filename, append_write) as f:
    for line in text:
        f.write(line)



# In[ ]:



