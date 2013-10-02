#model module to provide ajax inform
#
from google.appengine.ext import ndb


class Survey(ndb.Model):
    """Models an individual browser entry with an name, creator, engine and license"""
    code = ndb.StringProperty()
    name = ndb.StringProperty()
    resource = ndb.JsonProperty(repeated=True)
    script = ndb.StringProperty()
    script_type = ndb.StringProperty(choices=['python'])
    uploaded = ndb.DateTimeProperty(auto_now_add=True)


class Question(ndb.Model):
    id = ndb.IntegerProperty()
    text = ndb.StringProperty()
    test = ndb.KeyProperty()
    type = ndb.StringProperty(choices=['edit_text'])


class Answer(ndb.Model):
    id = ndb.IntegerProperty()
    value = ndb.StringProperty()
    question = ndb.KeyProperty()
    text = ndb.StringProperty()

class Result(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    answers = ndb.JsonProperty()
    test = ndb.KeyProperty()