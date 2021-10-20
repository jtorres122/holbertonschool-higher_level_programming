#!/usr/bin/python3
'''Module contains class Base'''
import json


class Base:
    '''Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor method of class Base'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Method returns JSON str rep'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
