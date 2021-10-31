#!/usr/bin/python3
'''Module contains function that writes an Object to a txt file'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function writes an Object to a txt file, using a JSON representation
    '''

    with open(filename, "w") as f:
        jsonstr = json.dumps(my_obj)
        f.write(jsonstr)
