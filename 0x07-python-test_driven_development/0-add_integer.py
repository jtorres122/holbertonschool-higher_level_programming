#!/usr/bin/python3
'''

Module contains a function that adds 2 integers

'''


def add_integer(a, b=98):
    '''
    Function verifies if inputs are ints and if so, returns the sum of both
    '''

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int or a is None:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return (a + b)
