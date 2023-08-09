class Square:
    def __init___(self, size=0):
      if not isinstance(size, int):
       raise TypeError("size must be an integer")
      if size < 0:
        raise ValueError("size must be >= 0")
      self.size = size
    def area(self):
      return self.size * self.size

    