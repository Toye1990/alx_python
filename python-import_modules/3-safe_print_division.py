#!/usr/bin/python3
if __name__ == "__main__":
 def safe_print_division(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
   return None
  finally:
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))   
    return result



