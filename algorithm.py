#------------- TWITTER RECOMMENDATION ALGORITHM ------------------
#------------------- BY JAMES DRAPER ------------------


#-------------- DESCRIPTION -----------------
# The file starts by asking the console to enter how many users they want, 
# and how many tweets each user should have.

# Then, the file asks the console to enter a name for the user, and then fill in each users tweets.
# This is repeated for the amount of users the console wanted.

# The file adds the tweets to the "userTweets" 2D array, and then associates the users name with the users tweets.

# The algorithm then creates a variable for the recommended tweets, and finds tweets by other users.
# After ensuring that the user is not recommended tweets that they have already made,
# Two sets are created, one for the users tweets and another for each unique tweet that the other users have made.
# The program checks if there are any common tweets between the primary user and the other users,
# if a user shares mutual tweets with the primary user, the program adds the unseen tweets to the recommendation array
# from the mutual connection to the primary user.

# The program then asks which user is receiving the recommendations 
# and runs the algorithm, printing the recommendations to the console


# Dimensions of 2D array for users and tweets
rows = int(input("Enter the number of users: "))
columns = int(input("Enter the number of tweets per user: "))


# dictionary to store user names
userTweets = {}

# Loop to fill the tweet array and assign names to each row of tweets
for i in range(rows):
    userNumber = i + 1
    print("")
    userName = input(f"Enter a name for User {userNumber}: ")

    # Creates an empty row for each user
    row = [] 

    #Input tweets for each user
    for j in range(columns):
        tweetNumber = j + 1
        element = input(f"Enter Tweet {tweetNumber} for {userName}: ")

        # Adds the element to the row
        row.append(element)  

    # Associate the user name with the row in the array for each users tweets
    userTweets[userName] = row  


# Print the user and their tweets (debug)
print("")
print("DEBUG TWEET LIST - IGNORE")
for userName, row in userTweets.items():
    print(f"{userName}: {row}")
print("")





# ---------------- ALGORITHM -----------------------

# Function to recommend tweets to a user based on shared interests
def recommendTweets(user, userTweets):

    # Create a variable for the recommended tweets
    recommendedTweets = []
    
    # Find tweets by other users
    for otherUser, tweets in userTweets.items():

        # Make sure that the user isn't recommended tweets by themselves
        if otherUser != user:

            # Find common tweets between the user and the other users
            commonTweets = set(userTweets[user]) & set(tweets)

            # Check if there are common tweets between each user
            if commonTweets:
                for tweet in tweets:

                    # Make sure the user hasn't seen the tweet, and it's not already recommended
                    if tweet not in userTweets[user] and tweet not in recommendedTweets:
                        
                        # Add the tweet to the list of recommended tweets
                        recommendedTweets.append(tweet)

    return recommendedTweets

# Select which user the recommendations will be tailored towards
primaryUser = input("Select a user to tailor tweet recommendations to: ")

# Create the variable for recommended tweets using the function
recommendedTweets = recommendTweets(primaryUser, userTweets)

# Show results
print("")
print(f"Recommended tweets for {primaryUser}:")
for tweet in recommendedTweets:
    print(tweet)
print("")
print("")
