import unittest
from google.appengine.ext import testbed

class StorageTestCase(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        # self.testbed.setup_env(app_id=application-id)
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
     
    def test_create_list(self):
        tlist = TList(id = "123", slug = "slug123")
        tlist.put()
        
        results = TestModel.all().fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual("123", results[0].id)
        self.assertEqual("slug123", results[0].slug)
         
         
