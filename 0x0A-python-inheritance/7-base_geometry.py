#!/usr/bin/python3
'''Module contains class BaseGeometry'''


class BaseGeometry:
    '''Class contains method area and integer validator'''

    def area(self):
        '''Method raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method validates that value is an int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
