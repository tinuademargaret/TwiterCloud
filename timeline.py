import tweepy
from tweepy import OAuthHandler

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_status  (sta):

    print(sta.text)

for status in tweepy.Cursor(api.user_timeline).items():
    # page is a list of statuses
    process_status(status)

#API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])