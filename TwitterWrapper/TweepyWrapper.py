#!/usr/bin/python
import tweepy
import re
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

    def recentMentions(self, minutes):
        mentions = self.twitter_api.mentions_timeline(
            count = 20,
            include_rts = 0)

        # TODO return only those from last n (param) minutes
        validExplorations = []
        for mention in mentions:
            s1 = mention.created_at
            s2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            FMT = "%Y-%m-%d %H:%M:%S"
            tdelta = datetime.strptime(s2, FMT) - s1

            if tdelta.seconds <= minutes*60 and self.tweetIsValid(mention):
                validExplorations.append(mention)

        return validExplorations

    def tweetIsValid(self, tweet):
        pattern = '([A-Fa-f0-9]{6}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{6})'
        planetCode = re.search(pattern, tweet.text)
        if planetCode:
            return True
        else:
            return False
