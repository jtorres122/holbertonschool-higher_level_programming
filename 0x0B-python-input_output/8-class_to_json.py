#!/usr/bin/python3
'''Module contains function that returns a dictionary description'''


def class_to_json(obj):
    '''
    Function returns the dict description with simple data struct
    for JSON serialization of an object
    '''

    return obj.__dict__
