"""
module will be used later
""" 
class Base:
 """
class base to used to manage id in this project and future project
""" 
 __nb_objects = 0
 def __init__(self, id=None):
  """
  A constructor to instantiate the instant value
  """ 
  if id is not None:
   self.id = id
  else:
   self.id = Base.__nb_objects + 1
   Base.__nb_objects += 1
   