"""Write a function that removes all characters c and C from a string.
Prototype: def no_c(my_string):
The function should return the new string"""

def no_c(my_string):
    all_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            all_string += char
    return all_string

