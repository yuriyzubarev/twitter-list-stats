import os
import json

class MockTwitterFetcher():
    
    def get_all_members_json(self, owner_screen_name, slug):
        return json.load(open(os.path.join(os.path.dirname(__file__), "mock_data/all_members.json")))
    
    