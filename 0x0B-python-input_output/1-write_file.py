#!/usr/bin/python3
'''Module contains a function that writes to a txt file'''


def write_file(filename="", text=""):
    '''
    Function writes a str to a txt file and returns
    the number of characters written
    '''

    with open(filename, "w") as f:
        f.write(text)

    return (len(text))
