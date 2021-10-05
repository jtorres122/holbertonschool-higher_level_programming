#!/usr/bin/python3
'''This module contains class Rectangle'''


class Rectangle:
    '''class Rectangle with attributes width and height defined and set'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''comment'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.print_symbol = self.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''comment'''
        return cls(size, size)

    def __str__(self):
        '''comment'''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for row in range(self.__height):
                for col in range(self.__width):
                    rectangle += str(self.print_symbol)
                rectangle += "\n"
            return rectangle[:-1]

    def __repr__(self):
        '''comment'''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''comment'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
