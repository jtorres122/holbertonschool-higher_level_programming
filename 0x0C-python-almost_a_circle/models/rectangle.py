#!/usr/bin/python3
'''Module contains class Rectangle that inherits from class Base'''
from models.base import Base


class Rectangle(Base):
    '''Child class of Base that defines a Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__width = value
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
