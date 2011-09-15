import unittest
from services import Twitter

import os
import json

class TwitterTestCase(unittest.TestCase):
    
    def setUp(self):
        self.twitter = Twitter(TwitterRepositoryMock())

    def test_lists_for_user(self):
        slugs = self.twitter.get_lists("bob")
        self.assertTrue(("53257043", "software-development") in slugs)

    def test_members_for_owner_screen_name_and_slug(self):
        members = self.twitter.get_members("bob", "software-development")
        self.assertTrue("rebeccaparsons" in members)
        self.assertTrue("mpoppendieck" in members)
        self.assertTrue("postwait" in members)

    def test_member_subscriber_counts(self):
        m, s = self.twitter.get_member_subscriber_counts("bob", "53257043")
        self.assertEqual(25, m)
        self.assertEqual(0, s)

class TwitterRepositoryMock():

    def get_lists_json(self, user):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/lists_for_user.json")))

    def get_members_json(self, owner_screen_name, slug):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/all_members.json")))

    def get_list_json(self, owner_screen_name, slug):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/list_show.json")))


