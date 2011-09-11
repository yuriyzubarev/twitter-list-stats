import unittest
from google.appengine.ext import testbed
from entities import TList
from entities import SnapShot
from datetime import datetime

class StorageTestCase(unittest.TestCase):
    
    def setUp(self):
        self.testbed = testbed.Testbed()
        # self.testbed.setup_env(app_id=application-id)
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
     
    def test_create_list(self):
        tlist = TList(id = "123", slug = "slug123")
        tlist.put()
        
        results = TList.all().fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual("123", results[0].id)
        self.assertEqual("slug123", results[0].slug)
         
    def test_create_snapshot(self):
        tlist = TList(id = "123", slug = "slug123")
        tlist.put()
        
        created_on = datetime.now()
        
        snap = SnapShot(members = 11, subscribers = 23)
        snap.tlist = tlist
        snap.created_on = created_on
        snap.put()

        results = SnapShot.all().fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual(11, results[0].members)
        self.assertEqual(23, results[0].subscribers)
        self.assertEqual(created_on, results[0].created_on)
        self.assertEqual("123", results[0].tlist.id)
        
        #test back-reference
        results = TList.all().fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual(1, results[0].snap_shots.count())
        self.assertEqual(11, results[0].snap_shots[0].members)
        


