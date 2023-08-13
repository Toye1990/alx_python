"""
Module Base import for inheritance purpose, this will validate the instance in
rectangle class. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora odio vitae cras blandit ut est integer nisl in accumsan himenaeos, facilisis eu maecenas lectus ante platea commodo curabitur fermentum et. 
Pellentesque euismod proin himenaeos nullam felis eros maecenas egestas tristique, pretium imperdiet morbi habitasse ullamcorper cras ad accumsan turpis, quis congue phasellus ultricies potenti volutpat varius torquent. 
Curae ante congue eu parturient imperdiet dui tempus penatibus, ultrices 
""" 
from models.base import Base
"""
Module Base import for inheritance purpose, this will validate the instance in
rectangle class. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora odio vitae cras blandit ut est integer nisl in accumsan himenaeos, facilisis eu maecenas lectus ante platea commodo curabitur fermentum et. 
Pellentesque euismod proin himenaeos nullam felis eros maecenas egestas tristique, pretium imperdiet morbi habitasse ullamcorper cras ad accumsan turpis, quis congue phasellus ultricies potenti volutpat varius torquent. 
Curae ante congue eu parturient imperdiet dui tempus penatibus, ultrices 
""" 
class Rectangle(Base):
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

