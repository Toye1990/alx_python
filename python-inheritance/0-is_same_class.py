#!/usr/bin/python3
"""
module to used later
"""

#used function to is_same_class() to confirm the instance of a class
def is_same_class(obj, a_class):
    #if the object is exactly an instance of the specified class
    if isinstance(obj, a_class):
        return True
    #otherwise False
    else:
        return False





'''class Phone:
    color = ""
    width = ""
    height = ""
    def __init__(self, mycolor, mywidth, myheight):
        self.width = mywidth
        self.height = myheight
        self.color = mycolor
    def makephone(self):
        return print("You can make calls")
callnow = Phone('red', 50, 40)
print(callnow.color)
print(callnow.width)
print(callnow.makephone())'''
        
