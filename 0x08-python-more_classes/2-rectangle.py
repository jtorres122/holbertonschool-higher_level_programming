#!/usr/bin/python3
'''This module contains class Rectangle'''


class Rectangle:
    '''class Rectangle with attributes width and height defined and set'''
    def __init__(self, width=0, height=0):
        '''comment'''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''comment'''
        return self.__width

    @width.setter
    def width(self, value):
        '''comment'''
        self.__width = value
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''comment'''
        return self.__height

    @height.setter
    def height(self, value):
        '''comment'''
        self.__height = value
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''comment'''
        area = self.__width * self.__height
        return area

    def perimeter(self):
        '''comment'''
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter
