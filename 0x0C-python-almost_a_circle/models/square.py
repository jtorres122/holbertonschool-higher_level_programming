#!/usr/bin/python3
'''Module contains class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Child class Square that inherits from parent class Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        self.width = size
        self.height = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Overriding str method to have specific return'''
        info = "[Square] ({}) {}/{} - {}"
        return info.format(self.id, self.x, self.y, self.width)
