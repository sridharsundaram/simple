from datamodel.learner import Learner
from datamodel.lesson1data import Lesson1Data
from google.appengine.ext import webapp
import os
from cookie import Cookie

class ManifestHandler(webapp.RequestHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'text/cache-manifest'
    self.response.headers['Cache-Control'] = 'max-age=0'
    
    # Retrieve tracking cookie to find stats for this user
    cookie, mobile, learner = Cookie.parse_maza(self.request.cookies)
    if learner:
      learner.Status = cookie
      learner.put()

    filename = os.path.join(os.path.dirname(__file__), "../html/lesson1.mf")
    f = open(filename, "r")
    text = f.read()
    self.response.out.write(text.replace('#', '#'))

  def post(self):
    self.get()   
    