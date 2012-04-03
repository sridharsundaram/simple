from google.appengine.ext import db
from base.formdb import Formdb
from datetime import date

"""
Word: Text, Picture, Audio
"""
class Word(Formdb):
  id_field = 'Text'
  Text = db.StringProperty()
  Picture = db.StringProperty()
  Audio = db.StringProperty()
  Group = db.BooleanProperty()
  Words = db.StringListProperty()