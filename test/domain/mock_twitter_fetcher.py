import os
import json

class MockTwitterFetcher():
    
    def get_lists_json(self, user):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/lists_for_user.json")))
        
    def get_members_json(self, owner_screen_name, slug):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/all_members.json")))
    
    def get_list_json(self, owner_screen_name, slug):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/list_show.json")))

