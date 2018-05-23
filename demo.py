import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'PLlGilgj5BcDaJXGLsf1Xqrj3'
consumer_secret= '0J5rRQlPWvcvibo5bvZeNxfH9AmZbs7a0lCldcONSP5gpTcTxB'

access_token='741181830750052352-MNYWn3bQTT0jvs2Yr2YEZUX6ARP3f3H'
access_token_secret='aFn8Oo1wE4wl6kEQpaST8Ua4Z9UicqWRW0KeXwasRuC14'

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
