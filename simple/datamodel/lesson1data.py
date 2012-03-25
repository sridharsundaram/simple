
from google.appengine.ext import db
from base.formdb import Formdb

"""
Learner: Name, MobileNumber, MobileDevice, UserAgent, MotherTongue, Sex, Age, Education, Profession, Status, JoinDate
"""
class Lesson1Data(Formdb):
  @staticmethod
  def get_data():
    sections = [    {'name': 'Mall',
                     'sound': 'Mall.mp3',
                     'img': 'Mall.jpg',
                     'list' : [ 
                       {'id': '11', 'question': "ATM.mp3", 'answer': "ATM.jpg"},
                       {'id': '12', 'question': "CheckoutCounter.mp3", 'answer': "CheckoutCounter.jpg"},
                       {'id': '13', 'question': "Cinema_Theatre.mp3", 'answer': "Cinema_Theatre.jpg"},
                       {'id': '14', 'question': "Escalator.mp3", 'answer': "Escalator.jpg"},
                       {'id': '15', 'question': "Food_Court.mp3", 'answer': "Food_Court.jpg"},
                       {'id': '16', 'question': "Mall.mp3", 'answer': "Mall.jpg"},
                       {'id': '17', 'question': "Metal_Detector.mp3", 'answer': "Metal_Detector.jpg"},
                       {'id': '18', 'question': "Shops.mp3", 'answer': "Shops.jpg"},
                       {'id': '19', 'question': "Rest_Rooms.mp3", 'answer': "Rest_Rooms.jpg"},
                       {'id': '20', 'question': "Security_Guard.mp3", 'answer': "Security_Guard.jpg"}] 
                     },
                     {
                      'name': 'Office',
                      'sound': 'Office.mp3',
                      'img': 'Office.jpg',
                      'list' : [ 
                       {'id': '1', 'question': "Coffee_Machine.mp3", 'answer': "Coffee_Machine.jpg"},
                       {'id': '2', 'question': "Cubicles.mp3", 'answer': "Cubicles.jpg"},
                       {'id': '3', 'question': "Desktop.mp3", 'answer': "Desktop.jpg"},
                       {'id': '4', 'question': "Meeting_Room.mp3", 'answer': "Meeting_Room.jpg"},
                       {'id': '5', 'question': "Photocopier.mp3", 'answer': "Photocopier.jpg"},
                       {'id': '6', 'question': "Presentation.mp3", 'answer': "Presentation.jpg"},
                       {'id': '7', 'question': "Printer.mp3", 'answer': "Printer.jpg"},
                       {'id': '8', 'question': "Reception.mp3", 'answer': "Reception.jpg"},
                       {'id': '9', 'question': "Sellotape.mp3", 'answer': "Sellotape.jpg"},
                       {'id': '10', 'question': "Office.mp3", 'answer': "Office.jpg"}] 
                     }]
    return {'section': sections}
