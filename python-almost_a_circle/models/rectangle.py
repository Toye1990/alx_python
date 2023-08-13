from base import Base
"""
module base import as inheritance for rectangle clase
""" 
class Rectangle(Base):
 __width = None
 __heigh = None
 __x = None
 __y = None
 
 """
 class rectangle to used to manage id in this project and future project
 """ 
 def __init__(self, width, height, x=0, y=0, id=None):
  """
 class constructor to initiate the rectangle
 """
  super().__init__(id)
  self.width = width
  self.height = height
  self.x = x
  self.y = y
  self.id = id
  
  @property
  def width(self):
   """Get the width of the rectangle."""
   return self.__width
  
  @width.setter
  def width(self, width):
   """Set the width of the rectangle."""
   self.__width = width

@property
def height(self):
 """Get the height of the rectangle."""
 return self.__height

@height.setter
def height(self, height):
  """Set the height of the rectangle."""
  self.__height = height

@property
def x(self):
 """Get the value x of the rectangle."""
 return self.__x

@x.setter
def x(self, x):
  """Set the x value of the rectangle."""
  self.__x = x

@property
def y(self):
 """Get the y value of the rectangle."""
 return self.__height

@y.setter
def y(self, y):
  """Set the y value of the rectangle."""
  self.__y = y

