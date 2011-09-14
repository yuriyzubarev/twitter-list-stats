from google.appengine.ext import db

class TList(db.Model):
    id = db.StringProperty(required = True)
    slug = db.StringProperty(required = True)
    user_screen_name = db.StringProperty(required = True)
    
class SnapShot(db.Model):
    tlist = db.ReferenceProperty(TList, collection_name = "snap_shots")
    created_on = db.DateTimeProperty(auto_now_add = True)
    members_count = db.IntegerProperty()
    subscribers_count = db.IntegerProperty()
    members = db.StringListProperty()