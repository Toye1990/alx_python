for i in range(100):
      if i == 99:
           print(i) 
      else:
        print("{}{}".format(
            "0" if i < 10 else "", i), end=", ")
