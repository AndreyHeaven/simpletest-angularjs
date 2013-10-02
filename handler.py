# -*- coding: utf-8 -*-
from google.appengine.ext.ndb import Key
import webapp2
import json
from model import *
from google.appengine.api import users
import yaml


class SurveyListHandler(webapp2.RequestHandler):
    def get(self):
        s_arr = []
        surveys = Survey.query().order(-Survey.uploaded).fetch()
        for s in surveys:
            s_arr.append({'code': s.key.urlsafe(), 'name': s.name})
        self.response.out.write(json.dumps(s_arr))

    def put(self):
        survey = json.loads(self.request.body)
        survey = self.parse_and_save(survey['text'], survey['resources'], survey['script'], survey['replace'])
        self.response.out.write(json.dumps({'key': survey.key.urlsafe()}))

    def parse_and_save(self, text, resources, script, replace):
        dataMap = yaml.load(text)
        resMap = yaml.load(resources)


        survey = Survey()
        if replace:
            survey = Key(urlsafe = replace['code']).get()
            for q in Question.query(Question.test == survey.key):
                for a in Answer.query(Answer.question == q.key):
                    a.key.delete()
                q.key.delete()
        survey.name = dataMap['name']
        survey.script = str(script)
        survey.resource = resMap
        survey.put()

        for i, q in enumerate(dataMap.get('questions')):
            question = Question()
            question.id = i
            question.test = survey.key
            question.text = q.get('text')
            question.type = q.get('type')
            question.put()
            if q.get('answers'):
                for a in q.get('answers'):
                    answer = Answer()
                    answer.question = question.key
                    answer.text = a.get('text')
                    answer.value = a.get('value')
                    answer.put()
        return survey





class AnswerHandler(webapp2.RequestHandler):
    def get(self, test_key):
        result = []
        survey = Key(urlsafe=test_key).get()
        for q in Question.query(Question.test == survey.key).order(Question.id):
            ans = []
            for a in Answer.query(Answer.question == q.key).order(Answer.id):
                ans.append({'id': a.id, 'text': a.text, 'value': a.value})
            result.append({'id': q.id, 'text': q.text, 'type': q.type, 'answers': ans})
        self.response.out.write(json.dumps(result))

class ResultHandler(webapp2.RequestHandler):
    def put(self, test_key):
        survey = Key(urlsafe=test_key).get()
        result = Result()
        result.test = survey.key
        result.answers = json.loads(self.request.body)
        kw = {}
        try:
            exec(survey.script, {'answers': result.answers, 'resource': survey.resource})
            result.text = kw['result']
        except Exception as e:
            print e
        result.put()
        self.response.out.write(json.dumps({'key': result.key.urlsafe()}))

    def get(self, result_key):
        result = Key(urlsafe=result_key).get()
        self.response.out.write(result.text)

class UserHandler(webapp2.RequestHandler):
    def get(self, action):

        if action == 'login':
            self.redirect(users.create_login_url())
        elif action == 'logout':
            self.redirect(users.create_logout_url())
        elif action == 'me' and users.get_current_user():
            self.response.out.write(json.dumps({
                'admin': users.is_current_user_admin(),
                'nickname': users.get_current_user().nickname()
            }))
        else:
            self.response.set_status(401)
