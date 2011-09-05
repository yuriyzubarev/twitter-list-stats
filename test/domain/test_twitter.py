import unittest
from twitter import Twitter
from mock_twitter_fetcher import MockTwitterFetcher

class MyTestCase(unittest.TestCase):
    def test_all_members_for_owner_screen_name_and_slug(self):
        twitter = Twitter(MockTwitterFetcher())
        members = twitter.get_all_members("bob", "family")
        if "rebeccaparsons" not in members:
            self.fail()
        if "mpoppendieck" not in members:
            self.fail()
        if "postwait" not in members:
            self.fail()

        
    def test_all_lists_for_owner_screen_name(self):
        pass