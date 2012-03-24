from google.appengine.ext import webapp
import simplejson

class OfficeData(webapp.RequestHandler):
  authorize = False
  
  def get(self):
    self.jsonData = {'allsounds' : [ 
                       {'id': '1', 'question': "Coffee_Machine.mp3", 'answer': "Coffee_Machine.jpg"},
                       {'id': '2', 'question': "Cubicles.mp3", 'answer': "Cubicles.jpg"},
                       {'id': '3', 'question': "Desktop.mp3", 'answer': "Desktop.jpg"},
                       {'id': '4', 'question': "Meeting_Room.mp3", 'answer': "Meeting_Room.jpg"},
                       {'id': '5', 'question': "Photocopier.mp3", 'answer': "Photocopier.jpg"},
                       {'id': '6', 'question': "Presentation.mp3", 'answer': "Presentation.jpg"},
                       {'id': '7', 'question': "Printer.mp3", 'answer': "Printer.jpg"},
                       {'id': '8', 'question': "Reception.mp3", 'answer': "Reception.jpg"},
                       {'id': '9', 'question': "Sellotape.mp3", 'answer': "Sellotape.jpg"},
                       {'id': '10', 'question': "Office.mp3", 'answer': "Office.jpg"}] }
    self.response.headers['Content-Type'] = 'application/json'
    self.response.headers['Content-Disposition'] = "attachment; filename=l.json"
    self.response.headers['Cache-Control'] = 'max-age=3600'
    self.response.out.write(simplejson.dumps(self.jsonData))
