ENGR298_contentreco_25movies

Script to generate content-based recommendations for all users
Input: movies.csv and ratings.csv
Output: create(or replace) table content_reco in database with recommendations for all users

1. Read the movies.csv file.
2. Create new dataframe df1 with genres as columns and movies as   
   rows. The 'ID' column contains the movieID. A '1' indicates presence of the genre and a '0' indicates the absence of the genre.
3. Read the ratings.csv file.
4. Accept as input, the number of movies in the movies file and the 
   number of users in the ratings file.
5. Create new dataframe df2 from the ratings file.
6. For each row in the file, check rating. If >=3, rating is set
   as 1. Else -1. Therefore for the movies not rated, it is set to 0.
7. Get list of all movies in the ratings file and movies file. It 
   is possible that there are movies in the movies.csv file that haven't been rated by any user. In that case, those movies won't be included in any recommendation. To make sure those movies are included, we do the following.
8. We create a new empty dataframe df2_new. This will include 
   columns for those movies too (movies not rated by any user). We iterate through the sorted list of rated_movies (rated_movies_list). We compare it against the corresponding movie ID in the sorted list of all movies (dataset_movies_list). If they match, we copy the column from df2 (contains ratings of all users for that movies) to df2_new. Else we insert a column of only 0s into df2_new in that position. 
9. Create user profile matrix df5. User profile matrix is created by
   computing the dot product of df3 and df4. Initially created dataframes df3 and df4 to drop the respective first columns from df2_new and df1 respectively. But eventually could do it without them. 
10.User profile matrix is a user x genre matrix (671 x 18) 
   genrated by computing the dot product of df2_new (user x movie matrix = 672 x 9127) and df1 (movie x genre = 9127 x 19). The first column needs to be removed from both to get a 671 x 18 matrix.
11.The scalar values in the df5 matrix represnt the user's 
   affinity towards each genre by looking collectively at all his ratings.
12.Create new empty dataframe df_content_reco to store 
   recommendations for all users. 
13.Iterate through df3, the binary rating matrix. For each user, 
   compute scores for each movie not rated by the user, based on the user's genre profile. Sort the movies based on the score and pick the top 25.
14.For each row, fetch the userid from df2_new. Create a new
   dataframe df6 (1 x 18), to hold the row from df5, i.e. the current user's profile.
15.Create another dataframe df_temp, with two columns, movieid and 
   value to hold the value for each movie (not rated by the user). Now iterate through each column (i.e. movie) of df3. If rating ==0, i.e. if the movie has not been rated by the user, compute the movie's score.
16.df7 - movie profile of the current movie, copied from df4 (1 x 
   18).
   df8 - transpose of df7 (18 x 1), to enable dot produvt
   df9 - dot product of df6 (1 x 18 user profile) and df8 (18 x 1 movie profile) gives a scalar value indicative of the user's interest in the movie calculated as an absolute value.
   This movieid and score are appended to df_temp.
17.df_content_reco_temp1 is created to hold the 25 movies with the 
   maximum score. These are then appended to df_content_reco.
18.df_content_reco is then written to the table content_reco. 
   Table will be replaced if it already exists.

Note: Run ENGR298_contentreco_11thMar2018_25movies_append.py to generate recommendations for a single (new) user. That will append a record to the content_reco table.