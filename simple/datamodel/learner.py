from google.appengine.ext import db
from base.formdb import Formdb
from base.formdb import ChoiceProperty

"""
Learner: Name, MobileNumber, MobileDevice, UserAgent, MotherTongue, Sex, Age, Education, Profession, Status, JoinDate
"""
class Learner(Formdb):
  id_field = 'MobileNumber'
  Name = db.StringProperty()
  MotherTongue = db.IntegerProperty() # ChoiceProperty([(0, None), (1, 'hindi'), (2, 'kannada')])
  MobileNumber = db.PhoneNumberProperty()
  MobileDevice = db.StringProperty()
  UserAgent = db.StringProperty()
  Sex = db.BooleanProperty()
  Age = db.IntegerProperty()
  Education = db.StringProperty()
  Profession = db.StringProperty()
  Status = db.StringProperty()
  JoinDate = db.DateProperty()
  