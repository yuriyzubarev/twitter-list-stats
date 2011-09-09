from google.appengine.ext import db

class TList(db.Model):
    id = db.StringProperty(required = True)
    slug = db.StringProperty(required = True)
    
class SnapShot(db.Model):
    tlist = db.ReferenceProperty(TList, collection_name = "snap_shots")
    created_on = db.DateTimeProperty(auto_now_add = True)
    members = db.IntegerProperty()
    subscribers = db.IntegerProperty()