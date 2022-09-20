from distutils.command.config import config
import tweepy
import configparser
import pandas as pd

# read configs 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['API_Key']
api_key_secret = config['twitter']['API_Key_Secret']

acess_token = config['twitter']['Access_Token']
access_token_secret = config['twitter']['Access_Token_Secret']

# authentication 
auth = tweepy.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(acess_token,access_token_secret)

api = tweepy.API(auth) 

public_tweets = api.home_timeline()

columns = ['Time', 'User', 'Tweet']

data = []

for tweet in public_tweets:
    data.append([tweet.created_at,tweet.user.screen_name, tweet.text])
    

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweets.csv')

