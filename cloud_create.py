import os
import tweepy
import numpy as np
from PIL import Image
from tweepy import OAuthHandler
from wordcloud import WordCloud, STOPWORDS

currdir = os.path.dirname(__file__)

consumer_key = '1tagTTrBcc9QYU3vXSb470eWg'
consumer_secret = 'D8h7fJxtkV0dlEploFRgJnsWNAkgucTIdrMpP9s9RxRMpiirSs'
access_token = '750396993017638912-vcilsltZJVwPlxhjrc2R1ggRY01infd'
access_secret = 'Vl4qAesDkAPCQ2WB99w2A6CQVHF0xbaVPu11PGazGW6ga'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_status(sta):
    # for status in tweepy.Cursor(api.user_timeline).items():

    return sta.text


def get_text(username):
    # for status in tweepy.Cursor(api.user_timeline).items():
    for status in tweepy.Cursor(api.user_timeline, id=username).items():
        # page is a list of statuses
        texts = process_status(status)
        yield texts


# print(timeline)


# API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])


def createwordcloud(text, shape, background_color):
    shape_to_file = dict(
        circle='Shapes/circle.jpg',
        hexagon='Shapes/hexagon-.jpg',
        heart='Shapes/heart.jpg',
        star='Shapes/star.jpg',
        triangle='Shapes/triangle.png'


    )
    mask = np.array(Image.open(os.path.join(currdir, shape_to_file[shape])))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color=background_color, max_words=200, mask=mask, stopwords=stopwords)
    wc.generate(text)
    wc.to_file(os.path.join(currdir, 'wc.png'))


createwordcloud(' '.join(list(get_text("victorshoaga"))), "star", "purple")



#Hail hydra!
