import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET'

access_token='ACCESS_TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

interest = input('What would you like to find out?:')

#Step 3 - Retrieve Tweets
public_tweets = api.search(interest)

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, "<===============")
    print("")
