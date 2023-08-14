"""
Module Base import for inheritance purpose, this will validate the instance in
rectangle class. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora odio vitae cras blandit ut est integer nisl in accumsan himenaeos, facilisis eu maecenas lectus ante platea commodo curabitur fermentum et. 
Pellentesque euismod proin himenaeos nullam felis eros maecenas egestas tristique, pretium imperdiet morbi habitasse ullamcorper cras ad accumsan turpis, quis congue phasellus ultricies potenti volutpat varius torquent. 
Curae ante congue eu parturient imperdiet dui tempus penatibus, ultrices 
""" 
from models.rectangle import Rectangle
"""
Module Base import for inheritance purpose, this will validate the instance in
rectangle class. Lorem ipsum dolor sit amet consectetur adipiscing elit tempus natoque faucibus viverra, litora odio vitae cras blandit ut est integer nisl in accumsan himenaeos, facilisis eu maecenas lectus ante platea commodo curabitur fermentum et. 
Pellentesque euismod proin himenaeos nullam felis eros maecenas egestas tristique, pretium imperdiet morbi habitasse ullamcorper cras ad accumsan turpis, quis congue phasellus ultricies potenti volutpat varius torquent. 
Curae ante congue eu parturient imperdiet dui tempus penatibus, ultrices 
""" 
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, id, x, y)
        self.width = size
        self.height = size
    def __str__(self):
        return ("[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
