"""
module will be used later
"""
def inherits_from(obj, a_class):
   """
    use function inherits_from() to confirm the instance of a class
    """
   if isinstance(obj, a_class):
      """
      use function isinstance() to confirm the instance of a class
      """
      return True
   if not isinstance(obj, type):
      """
      use function isinstance() with type as class argument to check if object is an instance of a class
      """
      return False
   while True:
      if issubclass(obj, type):
         return True
      obj = type(obj)

      if obj is object:
         return False