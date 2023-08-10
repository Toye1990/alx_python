def inherits_from(obj, a_class):
   if isinstance(obj, a_class):
      return True
   if not isinstance(obj, type):
      return False
   while True:
      if issubclass(obj, type):
         return True
      obj = type(obj)

      if obj is object:
         return False