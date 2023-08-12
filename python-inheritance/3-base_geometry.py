"""
module will be used later
"""
class BaseGeometry:
 """
 BaseGeometry class is outlined to determined details of functions and attributes used in the class
 """
 def __dir__(cls):
  return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
 



