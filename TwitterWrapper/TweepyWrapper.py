#!/usr/bin/python
import tweepy
from time import time, gmtime, strftime
from datetime import datetime
from Credentials.Credentials import *

"""
Wrapper for the Twitter API, just to keep it clean.
"""
class TwitterApi:
    # Login to twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_api = tweepy.API(auth)

    def postUpdate(self, status):
        self.twitter_api.update_status(status)

    def postUpdateWithImage(self, filePath, status):
        self.twitter_api.update_with_media(filePath, status=status)

    def recentMentions(self):
        mentions = self.twitter_api.mentions_timeline(
            count = 20,
            include_rts = 0)

        for mention in mentions:
            # print mention.created_at
            # # time.mktime()
            # print strftime("%Y-%m-%d %H:%M:%S", gmtime())
            s1 = mention.created_at
            s2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            FMT = "%Y-%m-%d %H:%M:%S"
            
            tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
            print tdelta

            print mention.text
            print mention.user.screen_name
