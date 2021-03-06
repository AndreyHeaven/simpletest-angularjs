# -*- coding: utf-8 -*-
import StringIO
from google.appengine.ext.ndb import Key
import sys
import webapp2
import json
from model import *
from google.appengine.api import users
import yaml
import traceback


def auth_required(fn):
    def wrapped(*args, **kwargs):
        if users.get_current_user():
            return fn(*args, **kwargs)
        else:
            args[0].response.set_status(401)
            return None
    return wrapped




class SurveyListHandler(webapp2.RequestHandler):
    def get(self):
        s_arr = []
        surveys = Survey.query().order(-Survey.uploaded).fetch()
        for s in surveys:
            s_arr.append({'code': s.key.urlsafe(), 'name': s.name})
        self.response.out.write(json.dumps(s_arr))

    #@auth_required
    def put(self):
        survey = json.loads(self.request.body)
        survey = self.parse_and_save(survey.get('text'), survey.get('resources'), survey.get('script'), survey.get('replace'))
        self.response.out.write(json.dumps(survey.to_json()))

    def parse_and_save(self, text, resources, script, replace):
        dataMap = yaml.load(text)
        resMap = yaml.load(resources)


        survey = Survey()
        if dataMap.get('code'):
            survey = Key(urlsafe = dataMap.get('code')).get()
        survey.name = dataMap.get('name')
        survey.script = str(script)
        survey.resource = resMap
        survey.questions = dataMap.get('questions')
        i = -1
        for q in survey.questions:
            if q.get('id') is None:
                q['id'] = i = i + 1

        survey.put()
        return survey


class AdminSurveyHandler(webapp2.RequestHandler):

    @auth_required
    def get(self, test_key):
        survey = Key(urlsafe=test_key).get()
        self.response.out.write(json.dumps({'code': survey.key.urlsafe(), 
                                            'script': survey.script,
                                            'text': yaml.safe_dump(survey.to_json(),
                                                                   encoding='utf-8',
                                                                   allow_unicode=True,
                                                                   default_flow_style=False),
                                            'resources': yaml.safe_dump(survey.resource,
                                                                        encoding='utf-8',
                                                                        allow_unicode=True, default_flow_style=False)
                                            }))


class AnswerHandler(webapp2.RequestHandler):
    def get(self, test_key):
        survey = Key(urlsafe=test_key).get()
        self.response.out.write(json.dumps(survey.questions))

class ResultHandler(webapp2.RequestHandler):
    def put(self, test_key):
        survey = Key(urlsafe=test_key).get()
        result = Result()
        result.test = survey.key
        result.answers = json.loads(self.request.body)
        code_out = StringIO.StringIO()
        code_err = StringIO.StringIO()
        try:
            # capture output and errors
            sys.stdout = code_out
            sys.stderr = code_err
            exec survey.script in {'answers': result.answers, 'resources': survey.resource}
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            result.text = code_out.getvalue()
        except Exception as e:
            traceback.print_exception(Exception, e, False)
            result.text = code_err.getvalue()
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            code_out.close()
            code_err.close()

        result.put()
        self.response.out.write(json.dumps({'key': result.key.urlsafe()}))

    def get(self, result_key):
        result = Key(urlsafe=result_key).get()
        self.response.out.write(result.text)

class UserHandler(webapp2.RequestHandler):


    def get(self, action):

        if action == 'login':
            self.redirect(users.create_login_url(self.request.referer))
        elif action == 'logout':
            self.redirect(users.create_logout_url(self.request.referer))
        elif action == 'me' and users.get_current_user():
            self.response.out.write(json.dumps({
                'admin': users.is_current_user_admin(),
                'nickname': users.get_current_user().nickname()
            }))
        else:
            self.response.set_status(401)

