

import os
import tweepy
from secrets import *
from time import gmtime, strftime
import time
import httplib
import json
from pprint import pprint

# ====== Individual bot configuration ==========================
bot_username = ''
logfile_name = bot_username + ".log"

# ==============================================================




conn = httplib.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/movie/latest?api_key=72a9e13ffcf773095ef24daba3324a34", payload)

res = conn.getresponse()
#data = res.read()
info = json.load(res)
moviedate = info["release_date"]
moviename = info["title"]
print moviename





date = time.strftime("%x")

systemdate = "20"+date[6:]+"-"+date[:2]+"-"+date[3:-3]
print systemdate
print moviedate


def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    text = "The movie '"+moviename+"' releases today ("+moviedate+") in theatres! *this is a test bot*" # Customized based on movie date
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)
 #if moviedate == systemdate:
tweet_text = create_tweet()
tweet(tweet_text)

