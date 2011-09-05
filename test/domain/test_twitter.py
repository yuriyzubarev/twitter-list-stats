import unittest
from twitter import Twitter
from mock_twitter_fetcher import MockTwitterFetcher

class MyTestCase(unittest.TestCase):
    def test_all_members_for_owner_screen_name_and_slug(self):
        twitter = Twitter(MockTwitterFetcher())
        members = twitter.get_all_members("bob", "family")
        if "marry" not in members:
            self.fail("marry not in members")
        if "scott" not in members:
            self.fail("scott not in members")

        
    def test_all_lists_for_owner_screen_name(self):
        pass