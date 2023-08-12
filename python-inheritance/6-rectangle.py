
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
    def area(self):
        return self._width * self._height