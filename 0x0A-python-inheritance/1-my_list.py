#!/usr/bin/python3
'''
Module contains a class that inherits
with a method that prints
'''


class MyList(list):
    ''' Class contains method that prints sorted  '''

    def print_sorted(self):
        ''' Method prints the list in ascending order '''
        print(sorted(self))
