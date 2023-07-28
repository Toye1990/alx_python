
def safe_print_division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
   print("You can not divide by zero")
   return None
  finally:
    print("{}".format(result) if 'result' in locals() else "Division is not valid")
  return result if 'result' in locals() else None



