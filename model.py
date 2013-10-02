#model module to provide ajax inform
#
from google.appengine.ext import ndb


class Survey(ndb.Model):
    name = ndb.StringProperty()
    resource = ndb.JsonProperty()
    script = ndb.BlobProperty()
    script_type = ndb.StringProperty(choices=['python'])
    uploaded = ndb.DateTimeProperty(auto_now_add=True)
    
    def to_json(self):
        result = []
        for q in Question.query(Question.test == self.key).order(Question.id):
            result.append(q.to_json())
        return {'code': self.key.urlsafe(), 'name': str(self.name), 'questions': result}



class Question(ndb.Model):
    id = ndb.IntegerProperty()
    text = ndb.StringProperty()
    test = ndb.KeyProperty()
    type = ndb.StringProperty(choices=['edit_text'])
    
    def to_json(self):
        ans = []
        for a in Answer.query(Answer.question == self.key).order(Answer.id):
            ans.append(a.to_json())
        return {'id': self.id, 'text': str(self.text), 'type': str(self.type), 'answers': ans}


class Answer(ndb.Model):
    id = ndb.IntegerProperty()
    value = ndb.StringProperty()
    question = ndb.KeyProperty()
    text = ndb.StringProperty()
    
    def to_json(self):
        return {'id': self.id, 'text': str(self.text), 'value': str(self.value)}

class Result(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    answers = ndb.JsonProperty()
    test = ndb.KeyProperty()