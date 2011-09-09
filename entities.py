from google.appengine.ext import db

class TList(db.Model):
    id = db.StringProperty(required = True)
    slug = db.StringProperty(required = True)
    
    