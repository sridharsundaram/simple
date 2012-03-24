from base.form_handler import FormHandler
from datamodel.learner import Learner

class LearnerHandler(FormHandler):
  html_form = 'html/learner.html'
  authorize = False
  cls = Learner

  def get(self):
    key = self.request.params.get('_key')
    if key:
      learner = Learner.retrieve(Learner, key)
    else:
      learner = Learner()
      
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
        """for variable in Variable.all().ancestor(template):
          type = self.request.params.get(variable.name)
          variable.setDomain(Domain.defaultDomain(Domain.externalToInternalType(type)))
          variable.put() """
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
