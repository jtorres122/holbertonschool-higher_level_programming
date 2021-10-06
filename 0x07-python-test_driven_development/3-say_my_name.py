#!/usr/bin/python3
'''

Module contains a function that prints out a first and last name

'''


def say_my_name(first_name, last_name=""):
    ''' Function prints two strings that are first and last names '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
