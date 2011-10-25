#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import urllib2
import json

class Twitter():

    """ 
    Service responsible for translating responses from twitter.com
    into application domain constructs.
    """
    
    def __init__(self, twitter_fetcher):
        self.fetcher = twitter_fetcher
        
    def get_lists(self, owner_screen_name):
        """ Returns a list of tuples of 'list id' and 'slug' for a given owner. """

        json_response = self.fetcher.get_lists_json(owner_screen_name)
        tlists = []
        for l in json_response["lists"]:
            tlists.append((l["id_str"], l["slug"]))
        return tlists
    
    def get_members(self, owner_screen_name, tlist_slug):
        """ Returns a list of screen names of all the members for a given owner and slug. """

        json_response = self.fetcher.get_members_json(owner_screen_name, tlist_slug)
        screen_names = []
        for user in json_response["users"]:
            screen_names.append(user["screen_name"])
        return screen_names
        
    def get_member_subscriber_counts(self, owner_screen_name, tlist_id):
        """ Returns a tuple of member count for a given owner and list id. """

        json_response = self.fetcher.get_list_json(owner_screen_name, tlist_id)
        members = json_response["member_count"]
        subscriber = json_response["subscriber_count"]
        return members, subscriber

if __name__ == '__main__':
    pass
