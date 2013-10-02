# -*- coding: utf-8 -*-
import StringIO
import datetime
from google.appengine.ext.ndb import Key
import sys
import webapp2
import json
from model import *
from google.appengine.api import users
import yaml

#output = StringIO.StringIO(buf="""
#---
#  name: "Тест на выявление причин ожирения и риска развития осложнений"
#  questions:
#    -
#      type: "edit_text"
#      text: "Ваш вес в кг"
#    -
#      type: "edit_text"
#      text: "Ваш рост в сантиметрах"
#    -
#      text: "Имеют ли Ваши ближайшие родственники избыточную массу тела?"
#      answers:
#        -
#          value: "2"
#          text: "Имеет мать"
#        -
#          value: "3"
#          text: "Имеет отец"
#        -
#          value: "1"
#          text: "Имеют оба"
#    -
#      text: "Ваш завтрак?"
#      answers:
#        -
#          value: "1"
#          text: "Нет завтрака (чашка кофе, чая)"
#        -
#          value: "2,5"
#          text: "Бутербродный завтрак"
#        -
#          value: "2"
#          text: "Яичница, колбаса, сосиски, ветчина"
#        -
#          value: "4"
#          text: "Овощной завтрак или фрукты, соки"
#        -
#          value: "5"
#          text: "Каша или творог"
#    -
#      text: "Объем завтрака?"
#      answers:
#        -
#          value: "0"
#          text: "Нет объема"
#        -
#          value: "3,5"
#          text: "200 г и менее"
#        -
#          value: "2"
#          text: "Более 200 г"
#    -
#      text: "Обед?"
#      answers:
#        -
#          value: "1"
#          text: "Нет обеда (перекус)"
#        -
#          value: "5"
#          text: "Мясо или рыба с гарниром до 200 г"
#        -
#          value: "3"
#          text: "200 – 400 г"
#        -
#          value: "2"
#          text: "&gt; 400 г"
#        -
#          value: "2"
#          text: "Мясной бульон"
#        -
#          value: "5"
#          text: "Овощной отвар"
#    -
#      text: "Ужин?"
#      answers:
#        -
#          value: "4"
#          text: "Мясо или рыба с гарниром до 200 г"
#        -
#          value: "2"
#          text: "Мясо или рыба с гарниром 300 – 500 г"
#        -
#          value: "1"
#          text: "Мясо или рыба с гарниром более 500 г"
#        -
#          value: "2"
#          text: "Пельмени менее 200 г"
#        -
#          value: "1"
#          text: "Пельмени более 200 г"
#        -
#          value: "0"
#          text: "Выпечка"
#    -
#      text: "Как поздно Вы ужинаете?"
#      answers:
#        -
#          value: "4"
#          text: "За 3 часа до сна"
#        -
#          value: "3"
#          text: "За 2 часа до сна"
#        -
#          value: "2"
#          text: "За 1 час до сна"
#        -
#          value: "1"
#          text: "Перед сном"
#    -
#      text: "Принимаете ли пищу ночью?"
#      answers:
#        -
#          value: "1"
#          text: "Да"
#        -
#          value: "4"
#          text: "Нет"
#    -
#      text: "Сколько раз в течение дня принимаете пищу (включая перекусы)?"
#      answers:
#        -
#          value: "1"
#          text: "2 раза"
#        -
#          value: "3"
#          text: "3 раза"
#        -
#          value: "4"
#          text: "4 – 5 раз"
#    -
#      text: "Как часто Вы употребляете кондитерские изделия?"
#      answers:
#        -
#          value: "1"
#          text: "Ежедневно"
#        -
#          value: "2"
#          text: "1 раз в неделю"
#        -
#          value: "3"
#          text: "1 раз в месяц"
#    -
#      text: "Ваши любимые гарниры?"
#      answers:
#        -
#          value: "1"
#          text: "Картофель"
#        -
#          value: "2"
#          text: "Макароны или вермишель"
#        -
#          value: "4"
#          text: "Каши"
#        -
#          value: "5"
#          text: "Овощи"
#    -
#      text: "Как часто Вы едите морскую рыбу и морепродукты?"
#      answers:
#        -
#          value: "5"
#          text: "Ежедневно"
#        -
#          value: "4"
#          text: "2 раза в неделю"
#        -
#          value: "3"
#          text: "1 раз в неделю"
#        -
#          value: "2"
#          text: "1 раз в месяц"
#        -
#          value: "1"
#          text: "Не ем"
#    -
#      text: "Когда Вы ложитесь спать?"
#      answers:
#        -
#          value: "5"
#          text: "До 22 часов"
#        -
#          value: "4"
#          text: "До 23 часов"
#        -
#          value: "3"
#          text: "До 24 часов"
#        -
#          value: "2"
#          text: "После 24 часов"
#        -
#          value: "1"
#          text: "После 1 часа ночи"
#    -
#      text: "Ходите ли Вы пешком ежедневно?"
#      answers:
#        -
#          value: "1"
#          text: "Не хожу"
#        -
#          value: "2"
#          text: "Менее 30 мин"
#        -
#          value: "3"
#          text: "От 1 ч до 1,5 ч"
#        -
#          value: "4"
#          text: "2 ч и более"
#    -
#      text: "Другие физические нагрузки?"
#      answers:
#        -
#          value: "3"
#          text: "Работа в саду"
#        -
#          value: "4"
#          text: "Подъем по лестнице"
#        -
#          value: "5"
#          text: "Посещение спортзала"
#    -
#      text: "Как часто Вы находитесь на свежем воздухе?"
#      answers:
#        -
#          value: "2"
#          text: "Менее 1 часа"
#        -
#          value: "3"
#          text: "Более 1 часа"
#        -
#          value: "4"
#          text: "Более 2 часов"
#    -
#      text: "Каков Ваш сон?"
#      answers:
#        -
#          value: "5"
#          text: "Быстро засыпаю, сплю хорошо"
#        -
#          value: "3"
#          text: "С трудом засыпаю, но сплю хорошо"
#        -
#          value: "2"
#          text: "С трудом засыпаю, часто просыпаюсь"
#    -
#      text: "Насколько психологически комфортна Ваша работа?"
#      answers:
#        -
#          value: "5"
#          text: "Комфортна"
#        -
#          value: "2"
#          text: "Не комфортна"
#    -
#      text: "Как Вы питаетесь на работе?"
#      answers:
#        -
#          value: "2"
#          text: "Коллективно"
#        -
#          value: "4"
#          text: "Раздельно"
#    -
#      text: "Подвержены ли Вы тревоге, депрессии?"
#      answers:
#        -
#          value: "2"
#          text: "Да"
#        -
#          value: "4"
#          text: "Нет"
#    -
#      text: "Проводился ли Вам контроль уровня сахара крови в ближайшее время? Были ли значения сахара выше нормы (> 5,5 ммоль/л)?"
#      answers:
#        -
#          value: "2"
#          text: "Да"
#        -
#          value: "4"
#          text: "Нет"
#    -
#      text: "Испытываете ли Вы сильное чувство жажды?"
#      answers:
#        -
#          value: "5"
#          text: "Редко"
#        -
#          value: "3"
#          text: "В жаркое время года"
#        -
#          value: "2"
#          text: "Постоянно"
#    -
#      text: "Имеется ли у Вас учащенное мочеиспускание?"
#      answers:
#        -
#          value: "5"
#          text: "Нет"
#        -
#          value: "4"
#          text: "Только днем"
#        -
#          value: "1"
#          text: "Днем и ночью"
#        -
#          value: "2"
#          text: "Только ночью"
#    -
#      text: "Имеется ли у Вас раздражение (зуд) в области половых органов?"
#      answers:
#        -
#          value: "2"
#          text: "Да"
#        -
#          value: "4"
#          text: "Нет"
#    -
#      text: "Как часто Вы испытываете головную боль?"
#      answers:
#        -
#          value: "2"
#          text: "ежедневно"
#        -
#          value: "3"
#          text: "1 – 2 раза в неделю"
#        -
#          value: "4"
#          text: "реже"
#        -
#          value: "5"
#          text: "не испытываю"
#    -
#      text: "Характер головной боли?"
#      answers:
#        -
#          value: "2"
#          text: "после физ. нагрузки"
#        -
#          value: "2"
#          text: "после стресса"
#        -
#          value: ""
#          text: "в области затылка"
#        -
#          value: ""
#          text: "в области висков"
#        -
#          value: ""
#          text: "разлитая боль"
#    -
#      text: "Бывает ли загрудинная и боль в области сердца?"
#      answers:
#        -
#          value: "2"
#          text: "после физ. нагрузки"
#        -
#          value: "2"
#          text: "после стресса"
#        -
#          value: "1"
#          text: "часто без видимой причины"
#    -
#      text: "Испытываете ли Вы чувство тревоги, страха?"
#      answers:
#        -
#          value: "3"
#          text: "редко"
#        -
#          value: "2"
#          text: "часто"
#        -
#          value: "5"
#          text: "не бывает"
#    -
#      text: "Бывает ли у Вас шум в голове?"
#      answers:
#        -
#          value: "3"
#          text: "редко"
#        -
#          value: "2"
#          text: "часто"
#        -
#          value: "5"
#          text: "не бывает"
#    -
#      text: "Бывает ли ощущение тошноты, озноба на фоне слабости?"
#      answers:
#        -
#          value: "3"
#          text: "редко"
#        -
#          value: "2"
#          text: "часто"
#        -
#          value: "5"
#          text: "не бывает"
#""")
##yaml.safe_dump(test, output, encoding='utf-8')
#dataMap = yaml.load(output)
#
#survey = Survey()
#survey.code = 'test1'
#survey.name = dataMap['name']
#survey.put()
#
#for i, q in enumerate(dataMap.get('questions')):
#    question = Question()
#    question.id = i
#    question.test = survey.key
#    question.text = q.get('text')
#    question.type = q.get('type')
#    question.put()
#    if q.get('answers'):
#        for a in q.get('answers'):
#            answer = Answer()
#            answer.question = question.key
#            answer.text = a.get('text')
#            answer.value = a.get('value')
#            answer.put()

class SurveyListHandler(webapp2.RequestHandler):
    def get(self):
        s_arr = []
        surveys = Survey.query().order(-Survey.uploaded).fetch()
        for s in surveys:
            s_arr.append({'code': s.key.urlsafe(), 'name': s.name})
        self.response.out.write(json.dumps(s_arr))


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
