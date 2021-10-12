#!/usr/bin/python3
''' Module contains a function that returns a list '''


def lookup(obj):
    '''
    Function returns a list of available attributes
    and methods of an object
    '''

    return (dir(obj))
