import logging
import os
import re
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

# Some mobile browsers which look like desktop browsers.
RE_MOBILE = re.compile(r"(iphone|ipod|blackberry|android|palm|symbian|windows\s+ce)", re.I)
RE_DESKTOP = re.compile(r"(windows|linux|os\s+[x9]|solaris|bsd)", re.I)
RE_BOT = re.compile(r"(spider|crawl|slurp|bot)", re.I)
RE_MOBILE_NUMBER = re.compile(r"[0-9]{10}", re.I)


class Register(webapp.RequestHandler):
          
  def is_desktop(self, user_agent):
    """
    Anything that looks like a phone isn't a desktop.
    Anything that looks like a desktop probably is.
    Anything that looks like a bot should default to desktop.
    
    """
    return not bool(RE_MOBILE.search(user_agent)) and \
      bool(RE_DESKTOP.search(user_agent)) or \
      bool(RE_BOT.search(user_agent))
  
  def get_user_agent(self, request):
    # Some mobile browsers put the User-Agent in a HTTP-X header
    return request.headers.get('HTTP_X_OPERAMINI_PHONE_UA') or \
           request.headers.get('HTTP_X_SKYFIRE_PHONE') or \
           request.headers.get('HTTP_USER_AGENT', '')
  
  def get(self):
    user_agent = self.request.user_agent
    if self.is_desktop(user_agent):
      logging.info("Desktop User Agent: %s", user_agent)
    else:
      logging.info("Mobile User Agent: %s", user_agent)
    self.response.headers['Content-Type'] = 'text/html'
    path = os.path.join(os.path.dirname(__file__), "registration_form.html")
    self.response.out.write(template.render(path, {}))

  def post(self):
    mobile = self.request.get('mobile')
    logging.info("Mobile: %s, User Agent: %s" % (mobile, self.request.user_agent))
    self.response.headers['Content-Type'] = 'text/html'
    if bool(RE_MOBILE_NUMBER.search(mobile)) and len(mobile) == 10:
      path = os.path.join(os.path.dirname(__file__), "registration_done.html")
    else:
      path = os.path.join(os.path.dirname(__file__), "registration_fail.html")
    self.response.out.write(template.render(path, {'mobile' : mobile}))
