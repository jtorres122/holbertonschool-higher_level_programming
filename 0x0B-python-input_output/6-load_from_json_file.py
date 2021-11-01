#!/usr/bin/python3
'''Module contains a function that creates an Obj from JSON file'''
import json


def load_from_json_file(filename):
    '''
    Function creates an Object from a JSON file
    '''

    with open(filename) as f:
        object = json.load(f)

    return object
