
"""
module will be used later
"""
class BaseGeometry:
 """
 BaseGeometry class to be used to raised an exception
"""
 def area(self):
    """
    BaseGeometry class to be used to raised an exception
    """
    raise Exception("area() is not implemented")
 def integer_validator(self, name, value):
    if not isinstance(value, int):
       TypeError(f"{name} must be an integer")
    if value <= 0:
        ValueError(f"{name} must be greater than")