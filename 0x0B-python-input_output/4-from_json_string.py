#!/usr/bin/python3
'''Module contains a function that returns an object repd by a JSON string'''
import json


def from_json_string(my_str):
    '''
    Function returns an object represented by a JSON string
    '''

    obj = json.loads(my_str)

    return (obj)
