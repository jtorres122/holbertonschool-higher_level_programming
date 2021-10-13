#!/usr/bin/python3
'''Module imports and contains classes BaseGeometry and Rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class is a child of BaseGeometry'''

    def __init__(self, width, height):
        '''Method inits instances'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
