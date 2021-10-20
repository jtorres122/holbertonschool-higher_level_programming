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

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Method assigns an argument to each attribute'''
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.size= args[1]
            if length >= 4:
                self.__x = args[3]
            if length >= 5:
                self.__y = args[4]
