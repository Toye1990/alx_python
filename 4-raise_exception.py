def raise_exception():
     try:
          raise_exception("where are you")
     except TypeError as x:
          print(x)
          