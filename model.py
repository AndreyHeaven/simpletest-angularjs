#model module to provide ajax inform
#
from google.appengine.ext import ndb


class Survey(ndb.Model):
    name = ndb.StringProperty()
    questions = ndb.JsonProperty()
    resource = ndb.JsonProperty()
    script = ndb.BlobProperty()
    script_type = ndb.StringProperty(choices=['python'])
    uploaded = ndb.DateTimeProperty(auto_now_add=True)
    
    def to_json(self):
        return {'code': self.key.urlsafe(), 'name': self.name, 'questions': self.questions}

class Result(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    answers = ndb.JsonProperty()
    test = ndb.KeyProperty()