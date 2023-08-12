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
        self.width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
    def area(self):
        return self.width * self.height
    def __str__(self):
        return ("[rectangle] {}/{}".format(self.width, self.height))
    def __repr__(self):
        return self.__str__() 

    