#!/usr/bin/python3
'''Module contains a function that appends a string at the end of a txt file'''


def append_write(filename="", text=""):
    '''
    Function that appends a string at the end of a text file
    and returns the number of characters added
    '''

    with open(filename, "a") as f:
        f.write(text)

    return(len(text))