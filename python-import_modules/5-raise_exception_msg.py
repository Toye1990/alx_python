#!/usr/bin/python3
if __name__ == "__main__":
 def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("")
except NameError as ne:
    print(ne)
