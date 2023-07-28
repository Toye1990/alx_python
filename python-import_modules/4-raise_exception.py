def raise_exception():
    raise TypeError("This is a type error")
try:
    raise_exception()
except TypeError as e:
    print("Error statement:", str(e))