from datamodel.learner import Learner
from datamodel.lesson1data import Lesson1Data
from google.appengine.ext import webapp
import os
import simplejson
import urllib

class ManifestHandler(webapp.RequestHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'text/cache-manifest'
    self.response.headers['Cache-Control'] = 'max-age=0'
    
    # Retrieve tracking cookie to find stats for this user
    cookie = urllib.unquote(self.request.cookies['maza'])
    if cookie:
      tracker = simplejson.loads(cookie)
      mobile_number = tracker['id']
      learner = Learner.retrieve(Learner, mobile_number)
      if learner:
        learner.Status = cookie
        learner.put()

    filename = os.path.join(os.path.dirname(__file__), "../html/lesson1.mf")
    f = open(filename, "r")
    text = f.read()
    self.response.out.write(text.replace('#', '#'))

  def post(self):
    self.get()   
    