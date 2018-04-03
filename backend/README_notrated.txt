ENGR298_not_rated_50_10thMarch2018_1

Input: movies.csv and ratings.csv
Output: Create/replce table not_rated_reco with random 50 movies not rated by each user in the table.

1. Read the movies.csv fill and store the movies in the dataframe 
   df_all_movies.
2. Read the ratings.csv file and create a dataframe 
   df_binary_rating to store the binary ratings. 
3. Create an empty dataframe df_not_rated_all to store movies for
   all users.
4. Iterate through the df_binary_rating dataframe. For each user,
   create two dataframes df_rated and df_not_rated. Iterate through each column (i.e. movie) from the binary ratings matrix. If movie is rated, append to df_rated.
4. Add the difference between df_all_movies and df_rated to 
   df_not_rated. Create another dataframe df_random to pick 50 movie at random from df_not_rated. Add these 50 movies to one row of df_not_rated_all alongwith the user ID.
5. Create/replace table not_rated_reco with data from
   df_not_rated_all.
   
Note: This is used to enable picking random movies in hybrid recommendations. Each time the user logs in, a different set of movies will chosen from within these 50 movies. To pick from a wider range, run this again, to get a new set of 50 un-rated movies for each user.