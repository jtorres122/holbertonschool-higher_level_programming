#!/usr/bin/python3
'''Module writes class Square with size attribute'''


class Square:
    '''Class verifies type and value of size'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if isinstance(value, tuple) is not True or value[0] < 0 or
        \value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        area = self.__size * self.__size
        return(area)

    def my_print(self):
        if self.__size == 0:
            print()

        for count in range(self.__position[1]):
            print()

        for row in range(self.__size):
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()
