#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import urllib2
import json

class Twitter():
    
    def __init__(self, twitter_fetcher):
        self.fetcher = twitter_fetcher
        
    def get_lists(self, user):
        json_response = self.fetcher.get_lists_json(user)
        slugs = []
        for l in json_response["lists"]:
            slugs.append(l["slug"])
        return slugs
    
    def get_members(self, owner_screen_name, slug):
        json_response = self.fetcher.get_members_json(owner_screen_name, slug)
        screen_names = []
        for user in json_response["users"]:
            screen_names.append(user["screen_name"])
        return screen_names
        
    def get_member_subscriber_counts(self, user, list_id):
        json_response = self.fetcher.get_list_json(user, list_id)
        members = json_response["member_count"]
        subscriber = json_response["subscriber_count"]
        return members, subscriber

if __name__ == '__main__':
    pass