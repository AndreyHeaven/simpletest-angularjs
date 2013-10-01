import datetime
from google.appengine.ext.ndb import Key
import webapp2
import json
from model import *
from google.appengine.api import users

survey = Survey()
survey.code = 'test1'
survey.name = 'Test1 '+str(datetime.datetime.now())
survey.put()

question = Question()
question.id = 1
question.test = survey.key
question.text = '1111111111111'
question.put()

answer = Answer()
answer.question = question.key
answer.text = '22222'
answer.code = '2'
answer.put()

question = Question()
question.id = 2
question.test = survey.key
question.text = '222222222222'
question.type = 'edit_text'
question.put()

class SurveyListHandler(webapp2.RequestHandler):
    def get(self):
        s_arr = []
        surveys = Survey.query().order(-Survey.uploaded).fetch()
        for s in surveys:
            s_arr.append({'code': s.code, 'name': s.name})
        self.response.out.write(json.dumps(s_arr))


class AnswerHandler(webapp2.RequestHandler):
    def get(self, test_key):
        result = []
        survey = Survey.query(Survey.code == test_key).get()
        for q in Question.query(Question.test == survey.key).order(Question.id):
            ans = []
            for a in Answer.query(Answer.question == q.key).order(Answer.id):
                ans.append({'id': a.id, 'text': a.text, 'code': a.code})
            result.append({'id': q.id, 'text': q.text, 'type': q.type, 'answers': ans})
        self.response.out.write(json.dumps(result))

class ResultHandler(webapp2.RequestHandler):
    def put(self, test_key):
        survey = Survey.query(Survey.code == test_key).get()
        result = Result()
        result.test = survey.key
        answers = json.loads(self.request.body)
        kw = {}
        try:
            exec survey.script in kw
            result.text = kw['result']
        except Exception:
            pass
        result.put()
        self.response.out.write(json.dumps({'key': result.key.urlsafe()}))

    def get(self, result_key):
        result = Key(urlsafe=result_key).get()
        self.response.out.write(result.text)

class UserHandler(webapp2.RequestHandler):
    def get(self, action):

        if action == 'login':
            self.redirect(users.create_login_url(self.request.uri))
        elif action == 'logout':
            self.redirect(users.create_logout_url(self.request.uri))
        elif action == 'me' and users.get_current_user():
            self.response.out.write(json.dumps({
                'admin': users.is_current_user_admin(),
                'nickname': users.get_current_user().nickname()
            }))
        else:
            self.response.set_status(401)
