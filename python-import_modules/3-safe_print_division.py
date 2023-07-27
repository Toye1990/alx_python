
def safe_print_division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
   print("You can not divide by zero")
   return None
  else:
    return result
  finally:
   result = safe_print_division(12, 2)
   print("{}".format(result))


