#!/usr/bin/python3
'''Module contains function that verifies instance of a class'''


def inherits_from(obj, a_class):
    '''Method verifies if obj is an instance of a_class'''

    if type(obj) != a_class and isinstance(obj, a_class) is True:
        return (True)
    else:
        return (False)
