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
    """class rectangle to used to manage id in this project and future project"""

    # Private instance attributes
    __width = None
    __height = None
    __x = None
    __y = None

    # Public getters and setters

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x-coordinate of the rectangle."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y-coordinate of the rectangle."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
      """area will be used to calculate the width and height of the rectangle clas."""
      return self.__width * self.__height
    
    def __str__(self):
      """Initialize string instance."""
      return ("[rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
            
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        
    def display(self):
       """using display function to print out #."""
       for i in range(self.height):
           for j in range(self.width):
               if j >= self.x and j < self.x + self.width:
                   if i >= self.y and i < self.y + self.height:
                      print("#", end="")
                   else:
                       print

    def update(self, *args):
        """Assign an argument to each attribute."""
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]


        
  
        
  
        