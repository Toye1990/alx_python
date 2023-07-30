#!/usr/bin/python3
if __name__ == "__main__":
 def safe_print_division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
   return None
  finally:
    print("{}".format(result))
    return result



