class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):

        if not isinstance(value, int):
            TypeError(f"<name> must be an integer")
        if self.value <= 0:
            ValueError(f"<name> must be greater than")