#!/usr/bin/env python3
import datetime

from core.mappers.Connections import Select, Insert

def user_info(username):
    info = Select().select_user_info(username)
    return {
        'first': info[0][0],
        'prev': info[0][1]
    }

def all_tweets():
    items = Select().select_all_posts()
    x = []
    for i in reversed(items):
        tweet = {
            'username': i[0],
            'date'    : i[1],
            'comment'   : i[2]
        }
        x.append(tweet)
    return x

def user_tweets(username):
    items = Select().select_all_user_posts(username)
    x = []
    for i in reversed(items):
        tweet = {
            'username': i[0],
            'date'    : i[1],
            'comment'   : i[2]
        }
        x.append(tweet)
    return x

def record_tweet(username,comment):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Insert().insert_tweet(username,date,comment)