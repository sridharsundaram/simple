from base.form_handler import FormHandler
from datamodel.learner import Learner

class HomeHandler(FormHandler):
  html_form = 'html/home.html'
  authorize = False
  cls = Learner

  def get(self):
    key = self.request.params.get('id')
    if key:
      learner = Learner.retrieve(Learner, key)
    else:
      self.redirect('/') # redirect to registration.
      
    self.template_values = {
      'learner' : learner,
    }
    FormHandler.get(self)

  def post(self):
    self.get()   
    
  # @param Formdb template - created or updated item
  def render(self, learner):
    action = self.request.params.get('action')
    if learner:
      self.template_values = {
        'learner': learner,                      
      }
    FormHandler.render(self, learner)  
