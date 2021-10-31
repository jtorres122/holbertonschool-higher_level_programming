#!/usr/bin/python3
'''Module contains a function that returs JSON representation of an object'''
import json


def to_json_string(my_obj):
    '''
    Function returs JSON rep of an object(string)
    '''

    jsonstr = json.dumps(my_obj)

    return (jsonstr)
