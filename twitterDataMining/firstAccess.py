#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:43:49 2019

@author: ryan.nanson
"""

import json
import tweepy
from tweepy import OAuthHandler

# Aunthenication Details
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_secret = 'your-access-secret'

 
def process_or_store(tweet):
    print(json.dumps(tweet))
    
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# Print the response
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

## Store the responses
    
# Process a single status
for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)

# List all followers
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# List all tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
