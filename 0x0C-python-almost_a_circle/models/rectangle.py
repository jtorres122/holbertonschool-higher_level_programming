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

    def area(self):
        '''Method returns the area value of the rectangle'''
        area = self.__width * self.__height
        return (area)

    def display(self):
        '''Method prints the Rectangle instance with the character #'''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        '''Overriding str method to have specific return'''
        info = "[Rectangle] ({}) {}/{} - {}/{}"
        return info.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        '''Method assigns an argument to each attribute'''
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass
