from google.appengine.ext import db
from base.formdb import Formdb
from datetime import date

"""
Learner: Name, MobileNumber, MobileDevice, UserAgent, MotherTongue, Sex, Age, Education, Profession, Status, JoinDate
"""
class Learner(Formdb):
  id_field = 'MobileNumber'
  Name = db.StringProperty()
  MotherTongue = db.IntegerProperty(default = 2) # choices = Set('hindi', 'kannada')
  MobileNumber = db.PhoneNumberProperty() # primary key
  MobileDevice = db.StringProperty()
  UserAgent = db.StringProperty()
  Sex = db.BooleanProperty(default = False) # choices = Set(Male, Female)
  Age = db.IntegerProperty()
  Education = db.StringProperty()
  Profession = db.StringProperty()
  Status = db.StringProperty()
  JoinDate = db.DateProperty(default = date.today())
  Channel = db.StringProperty()
  