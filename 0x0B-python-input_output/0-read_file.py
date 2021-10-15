#!/usr/bin/python3
'''Module contains a function that reads a text file'''

def read_file(filename=""):
    '''Function reads a text file and prints to stdout'''

    with open(filename, encoding="utf-8") as f:
        print(f.read())
