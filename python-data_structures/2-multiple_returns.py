''''Write a function that returns a tuple with the length of a string 
and its first character.
Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None'''

def multiple_returns(sentence):
    if not sentence:
     return (0, None)
    else:
       return (len(sentence), sentence[0])
    

    