#!/usr/bin/python3
'''Module writes class Square with size attribute'''


class Square:
    '''Class verifies type and value of size'''
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return(area)
