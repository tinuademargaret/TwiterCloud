import tweepy
from tweepy import OAuthHandler

consumer_key = '1tagTTrBcc9QYU3vXSb470eWg'
consumer_secret = 'D8h7fJxtkV0dlEploFRgJnsWNAkgucTIdrMpP9s9RxRMpiirSs'
access_token = '750396993017638912-vcilsltZJVwPlxhjrc2R1ggRY01infd'
access_secret = 'Vl4qAesDkAPCQ2WB99w2A6CQVHF0xbaVPu11PGazGW6ga'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_status(sta):
    #for status in tweepy.Cursor(api.user_timeline).items():

    return sta.text


#for status in tweepy.Cursor(api.user_timeline).items():
#for status in tweepy.Cursor(api.user_timeline, id="victorshoaga").items():

    # page is a list of statuses
    #timeline = process_status(status)
    #print(timeline)

#API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
def get_text(username):
#for status in tweepy.Cursor(api.user_timeline).items():
    for status in tweepy.Cursor(api.user_timeline, id=username).items():
        texts = []
        # page is a list of statuses
        texts.append(process_status(status))
    return texts


print(get_text('victorshoaga'))

