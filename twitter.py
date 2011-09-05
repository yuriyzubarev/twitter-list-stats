#!/usr/bin/env python
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import urllib2
import json

class Twitter():
    
    def __init__(self, twitter_fetcher):
        self.fetcher = twitter_fetcher
        
    def get_all_members(self, owner_screen_name, slug):
        json_response = self.fetcher.get_all_members_json(owner_screen_name, slug)
        screen_names = []
        for user in json_response["users"]:
            screen_names.append(user["screen_name"])
        return screen_names

if __name__ == '__main__':
    pass