ENGR298_coccurencereco_23Feb2018_1_25_recos

Input: Cooccurence.csv file containing 20/25 movies cooccured most with each movie in the ratings.csv file.
Output: Create/replace cooccurence_reco_25 with top 25 recommendations for each user based on the top movie cooccurences.

1. Accept as input, the number of movies in the file, per movie. 
   i.e. the number of movies that are in the file, for each movie.
2. Accept as input number of recommendations to be generated per
   user (25).
3. Create a new dataframe df_movie_movie to hold the top movies 
   that cooccured with movie.
4. Read through the file and fill df_movie_movie. Each row in this 
   dataframe corresponds to each movie and each column corresponds to the movies that cooccured. 
5. Read the ratings file and generate a binary rating matrix. The
   dataframe df_binary_rating is created to hold this matrix. A '1' indicates a user has rated the movie and a '0' indicates the movie was not rated by the user.
6. Create dataframe df_cooccur_reco to store all user's 
   recommendations. Iterate through each row in df_binary_rating. For each row, create two dataframes, df_temp_movie_rank and df_temp_final. df_temp_movie_rank will store the movieid and scores for all movies that cooccured with all the movies rated by the user. For eg, if the user has rated 10 movies and there are 20 movies in the file for each movie, df_temp_movie_rank will have 200 rows, with possible multiple entries for the same movie.
7. We sum the scores by movie from df_temp_movie_rank and sort 
   them in decreasing order.
8. From df_temp_movie_rank, we iterate through each movie, if not 
   rated by the user (i.e. it can be recommended), and add a row to df_temp_final.
9. All 25 movies(rows) from df_temp_final are copied into a single 
   row for the user into df_cooccur_reco.
10. Then the data is written to the table cooccurence_reco_25. 

Note: Table will be replaced if already exists.