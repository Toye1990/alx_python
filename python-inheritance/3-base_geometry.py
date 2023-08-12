#write an empty class
class BaseGeometry:
 def __dir__(cls):
  return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
 
base = BaseGeometry()
print(dir(base))


