#!/usr/bin/python3
'''Module contains class Student'''


class Student:
    '''class contains instantiation and __dict__'''

    def __init__(self, first_name, last_name, age):
        '''object instantiation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Method prints out __dict__ of class Student'''
        new_dictionary = {}
        if attrs is None:
            return self.__dict__
        else:
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dictionary[k] = v
            return new_dictionary
