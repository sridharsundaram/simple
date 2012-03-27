import simplejson
import urllib
from datamodel.learner import Learner
from datetime import date

class Cookie:
  
  # @return (cookie, mobile, learner)
  @staticmethod 
  def parse_maza(cookies):
    # Retrieve tracking cookie to find stats for this user
    
    cookie = cookies['maza']
    if not cookie:
      return (None, None, None)
    
    cookie = urllib.unquote(cookies['maza'])
    if cookie:
      tracker = simplejson.loads(cookie)
      mobile = tracker['id']
      learner = Learner.retrieve(Learner, mobile)
      return (cookie, mobile, learner)
    return (None, None, None)
  
  @staticmethod
  def get_maza_cookie_str(status):
    return 'maza=' + urllib.quote(status) + ';path=/;'
