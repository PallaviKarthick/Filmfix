ENGR298_contentreco_27thMar2018_syntheticdata_1

Script to generate synthetic data for new user to test content based
recommendations.
Input: User ID, User Type (New/Existing), Genre 1, 2 and 3 (between 1 and 18)
Output:ratings_<userid>.csv file

1. Accept the userid and usertype as input.
2. Accept as input three genres (between 1 and 18).
3. Accept as input the total number of movies to be added
4. For existing user, create a separate list called rated_list.
   Read the ratings.csv file and append to this list, all movie IDs already rated by the user.
5. Read the movies csv file.
6. Generate df1 - a movie- genre matrix comprising of movies as
   rows and genres as column. A '1' indicates presence of the genre and '0' indicates absence of the genre. The first column 'ID' holds the movie ID. For an existing user, add the movie ID, if only not present in the rated_list.
7. Two new columns 'Total' and 'Chosen' indicate how many genres
   are defined and how many of the input genres are present for that movie. For e.g., if a movie has genres Action, Adventure, Fantasy, Thriller and the chosen genres (user input) are Comedy, Drama and Action, Total would be 4 and Chosen would be 1. 
8. Create empty lists to store different combinations of genres. 
   Since movies with higher ratio of genres chosen : genres total should be rated higher, we create different lists
   list1 = [] # Total-3; Chosen-3
   list2 = [] # Total-2; Chosen-2
   list3 = [] # Total-1; Chosen-1
   list4 = [] # Total-3; Chosen-2
   list5 = [] # Total-2; Chosen-1
   list6 = [] # Total-3; Chosen-1
   list7 = [] # Total>3; Chosen-3
   list8 = [] # Total>3; Chosen-2
   list9 = [] # Total>3; Chosen-1
9. Iterate through df1 and populate all lists based on 'Total'
   and 'Chosen' values.
10. Shuffle all lists seperately to ensure a good mix of movies,
   instead of always picking movies from the beginning.
11.Create a new empty lost to hold all the recommendations.
12.Check if number of movies in list1,list2 and list3 combined
   are enough or not.
13.If yes, pop movies from list1, list2 and list3 iteratively and
   add to final list.
14.If not, add all elements from list1, list2 and list3.
   Then add  elements from list4, list5, list 7 and list8 one after the other.
15.Write data from string into csv file. If file for the user 
   already exists, rows will be appended. Else, new file will be created.
16.Care should be taken to append rows to existing file. Since the 
   script id only for new users, movies will be picked from the complete movies list. If the script is run once for a user, we must ensure while running it subsequently for the same user, the genres are not repeated. Even then, we must ensure the file doesn't have multiple entries for the same movie.