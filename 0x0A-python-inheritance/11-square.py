#!/usr/bin/python3
'''Module imports and contains classes BaseGeometry, Rectangle and Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Child class of Rectangle'''

    def __init__(self, size):
        '''Method inits instance'''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''Method calculates the area of a square'''
        area = self.__size * self.__size
        return (area)

    def __str__(self):
        '''Method str of class Square'''
        return ("[Square] {}/{}".format(self.__size, self.__size))
