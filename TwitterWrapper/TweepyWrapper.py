#!/usr/bin/python
import tweepy
from Credentials.Credentials import *

"""
Wrapper for the Twitter API, just to keep it clean.
"""
class TwitterApi:
    # Login to twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_api = tweepy.API(auth)

    def PostUpdate(self, status):
        self.twitter_api.update_status(status)

    def post_update_with_image(self, file_path, status):
        self.twitter_api.update_with_media(file_path, status=status)

    def recentMentions(self):
        mentions = self.twitter_api.mentions_timeline(
            count = 20,
            include_rts = 0)

        for mention in mentions:
            print mention.text
            print mention.user.screen_name
