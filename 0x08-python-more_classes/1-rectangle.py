#!/usr/bin/python3
'''This module contains class Rectangle'''


class Rectangle:
    '''class Rectangle with attributes width and height defined and set'''
    def __init__(self, width=0, height=0):
        '''comment'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''comment'''
        return self.__width

    @width.setter
    def width(self, value):
        '''comment'''
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''comment'''
        return self.__height

    @height.setter
    def height(self, value):
        '''comment'''
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
