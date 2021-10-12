#!/usr/bin/python3
'''Module contains function that verifies instance of a class'''


def is_same_class(obj, a_class):
    '''Method verifies if obj is exactly an instance of a_class'''

    if type(obj) == a_class:
        return (True)
    else:
        return (False)
