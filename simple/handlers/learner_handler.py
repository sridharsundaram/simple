from base.form_handler import FormHandler
from datamodel.learner import Learner
from google.appengine.ext import db

class LearnerHandler(FormHandler):
  html_form = 'html/learner.html'
  authorize = False
  cls = Learner

  def get(self):
    key = self.request.params.get('_key')
    learner = None
    if key:
      learner = Learner.retrieve(Learner, key)
    elif self.request.params.get(Learner.id_field):
      idval = self.request.params.get(Learner.id_field)
      learner = Learner.all().filter("MoblieNumber = ", idval).fetch(1)
    if not learner:
      learner = Learner()
      if idval:
        learner.MobileNumber = db.PhoneNumber(idval)
      
    self.template_values = {
      'learner' : learner,
      'deleted': False,
    }
    FormHandler.get(self)

  def post(self):
    learner = self.processPostData()
    learner.put()
    key = self.request.params.get('_key')
    action = self.request.params.get('action')
    if key:
      if action == 'Delete':
        learner.delete()
    else:
      pass
    self.render(learner)
    
    
  # @param Formdb template - created or updated item
  def render(self, learner):
    action = self.request.params.get('action')
    if learner:
      if action == 'Submit' or action == 'Delete':
        self.html_form = "html/learner.html"
      self.template_values = {
        'learner': learner,                      
        'deleted': action == 'Delete',
      }
    FormHandler.render(self, learner)  
