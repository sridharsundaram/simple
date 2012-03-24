import logging

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class FormPolydb(polymodel.PolyModel):
  id_field = None
  
  @staticmethod
  def type(instance, field):
    return Formdb.type(instance,field)
  
  @staticmethod
  def retrieve(cls, my_id):
    logging.info("Retrieving: ")
    logging.info(my_id)
    entity = Formdb.retrieve(cls, my_id)
    logging.info('Retrieval done')
    return entity    
  
class Formdb(db.Model):
  id_field = None

  @staticmethod
  def type(instance, field):
    typestr = str(instance._properties[field].__class__)
    components = typestr.replace("'>", "").split('.')
    return components[len(components)-1]

  @staticmethod
  def retrieve(cls, my_id):
    
    # my_id is the key of the record if id_field is missing
    if not cls.id_field:
      return db.get(my_id)
    
    query = cls.gql("WHERE " + cls.id_field + " = :1", my_id)

    for result in query:
      return result

    logging.info("Retrieval failed for: " + my_id)
    return None


class ChoiceProperty(db.IntegerProperty):
  """A property for efficiently storing choices made from a finite set.

  This works by mapping each choice to an integer.  The choices must be hashable
  (so that they can be efficiently mapped back to their corresponding index).

  Example usage:

  >>> class ChoiceModel(db.Model):
  ...   a_choice = ChoiceProperty(enumerate(['red', 'green', 'blue']))
  ...   b_choice = ChoiceProperty([(0,None), (1,'alpha'), (4,'beta')])

  You interact with choice properties using the choice values:

  >>> model = ChoiceModel(a_choice='green')
  >>> model.a_choice
  'green'
  >>> model.b_choice == None
  True
  >>> model.b_choice = 'beta'
  >>> model.b_choice
  'beta'
  >>> model.put() # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'ChoiceModel', ...)

  >>> model2 = ChoiceModel.all().get()
  >>> model2.a_choice
  'green'
  >>> model.b_choice
  'beta'

  To get the int representation of a choice, you may use either access the
  choice's corresponding attribute or use the c2i method:
  >>> green = ChoiceModel.a_choice.GREEN
  >>> none = ChoiceModel.b_choice.c2i(None)
  >>> (green == 1) and (none == 0)
  True

  The int representation of a choice is needed to filter on a choice property:
  >>> ChoiceModel.gql("WHERE a_choice = :1", green).count()
  1
  """
  def __init__(self, choices, make_choice_attrs=True, *args, **kwargs):
    """Constructor.

    Args:
      choices: A non-empty list of 2-tuples of the form (id, choice). id must be
        the int to store in the database.  choice may be any hashable value.
      make_choice_attrs: If True, the uppercase version of each string choice is
        set as an attribute whose value is the choice's int representation.
    """
    super(ChoiceProperty, self).__init__(*args, **kwargs)
    self.index_to_choice = dict(choices)
    self.choice_to_index = dict((c,i) for i,c in self.index_to_choice.iteritems())
    if make_choice_attrs:
      for i,c in self.index_to_choice.iteritems():
        if isinstance(c, basestring):
          setattr(self, c.upper(), i)

  def get_choices(self):
    """Gets a list of values which may be assigned to this property."""
    return self.choice_to_index.keys()

  def c2i(self, choice):
    """Converts a choice to its datastore representation."""
    return self.choice_to_index[choice]

  def __get__(self, model_instance, model_class):
    if model_instance is None:
      return self
    index = super(ChoiceProperty, self).__get__(model_instance, model_class)
    return self.index_to_choice[index]

  def __set__(self, model_instance, value):
    try:
      index = self.c2i(value)
    except KeyError:
      raise db.BadValueError('Property %s must be one of the allowed choices: %s' %
                          (self.name, self.get_choices()))
    super(ChoiceProperty, self).__set__(model_instance, index)

  def get_value_for_datastore(self, model_instance):
    # just use the underlying value from the parent
    return super(ChoiceProperty, self).__get__(model_instance, model_instance.__class__)

  def make_value_from_datastore(self, value):
    if value is None:
      return None
    return self.index_to_choice[value]

