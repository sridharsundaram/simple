from google.appengine.ext import webapp
import simplejson

class MallData(webapp.RequestHandler):
  authorize = False
  
  def get(self):
    self.jsonData = {'allsounds' : [ 
                       {'id': '1', 'question': "ATM.mp3", 'answer': "ATM.jpg"},
                       {'id': '2', 'question': "CheckoutCounter.mp3", 'answer': "CheckoutCounter.jpg"},
                       {'id': '3', 'question': "Cinema_Theatre.mp3", 'answer': "Cinema_Theatre.jpg"},
                       {'id': '4', 'question': "Escalator.mp3", 'answer': "Escalator.jpg"},
                       {'id': '5', 'question': "Food_Court.mp3", 'answer': "Food_Court.jpg"},
                       {'id': '6', 'question': "Mall.mp3", 'answer': "Mall.jpg"},
                       {'id': '7', 'question': "Metal_Detector.mp3", 'answer': "Metal_Detector.jpg"},
                       {'id': '8', 'question': "Shops.mp3", 'answer': "Shops.jpg"},
                       {'id': '9', 'question': "Rest_Rooms.mp3", 'answer': "Rest_Rooms.jpg"},
                       {'id': '10', 'question': "Security_Guard.mp3", 'answer': "Security_Guard.jpg"}] }
    self.response.headers['Content-Type'] = 'application/json'
    self.response.headers['Content-Disposition'] = "attachment; filename=l.json"
    self.response.headers['Cache-Control'] = 'max-age=3600'
    self.response.out.write(simplejson.dumps(self.jsonData))
