
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
        self._width = 0
        self._height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return "[rectangle] {} - {}".format(self._width, self._height)
    
    def __str__(self):
        return "[rectangle] {}/{}".format(self._width, self._height)