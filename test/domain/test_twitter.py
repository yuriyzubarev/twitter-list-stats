import unittest
from twitter import Twitter
from mock_twitter_fetcher import MockTwitterFetcher

class MyTestCase(unittest.TestCase):

    def test_all_lists_for_user(self):
        twitter = Twitter(MockTwitterFetcher())
        slugs = twitter.get_lists("bob")
        self.assertTrue("software-development" in slugs)

    def test_all_members_for_owner_screen_name_and_slug(self):
        twitter = Twitter(MockTwitterFetcher())
        members = twitter.get_members("bob", "family")
        self.assertTrue("rebeccaparsons" in members)
        self.assertTrue("mpoppendieck" in members)
        self.assertTrue("postwait" in members)

        
