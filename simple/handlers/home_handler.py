from base.form_handler import FormHandler
from datamodel.learner import Learner
from datamodel.lesson1data import Lesson1Data
from google.appengine.ext import webapp
import os
import simplejson

class HomeHandler(webapp.RequestHandler):

  def get(self, mobile_number):
    learner = Learner.retrieve(Learner, mobile_number)
    if not learner:
      self.redirect('/') # redirect to registration.
      
    jsonData = {
      'learner' : { 'MobileNumber' : learner.MobileNumber},
      'lesson': Lesson1Data.get_data()
    }
    jsonDataStr = simplejson.dumps(jsonData)
    self.response.headers['Content-Type'] = 'text/html'
    self.response.headers['Cache-Control'] = 'max-age=3600'

    filename = os.path.join(os.path.dirname(__file__), "../html/lesson1.html")
    f = open(filename, "r")
    text = f.read()
    self.response.out.write(text.replace('{{JSONDATA}}', jsonDataStr))

  def post(self):
    self.get()   
    