# BASIC TWITTER RECOMMENDATION ALGORITHM



## DESCRIPTION
The file starts by asking the console to enter how many users they want, 
and how many tweets each user should have

Then, the file asks the console to enter a name for the user, and then fill in each users tweets.
This is repeated for the amount of users the console wanted.

The file adds the tweets to the "userTweets" 2D array, and then associates the users name with the users tweets.

The algorithm then creates a variable for the recommended tweets, and finds tweets by other users.
After ensuring that the user is not recommended tweets that they have already made,
Two sets are created, one for the users tweets and another for each unique tweet that the other users have made.
The program checks if there are any common tweets between the primary user and the other users,
if a user shares mutual tweets with the primary user, the program adds the unseen tweets to the recommendation array
from the mutual connection to the primary user.

The program then asks which user is receiving the recommendations 
and runs the algorithm, printing the recommendations to the console
