"""
module will be used later
""" 
class BaseGeometry:
    """
    class BaseGeometry to reused
    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):

        if not isinstance(value, int):
            TypeError(f"<name> must be an integer")
        if self.value <= 0:
            ValueError(f"<name> must be greater than")
class Rectangle(BaseGeometry):
    """
    class BaseGeometry reused
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return ("[rectangle] {}/{}".format(self.__width, self.__height))
    def __repr__(self):
        return "rectangle {} {}".format(self.__width, self.__height)

    