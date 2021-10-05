#!/usr/bin/python3


def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for row in range(size):
            for col in range(size):
                print("#", end="")
            print()
