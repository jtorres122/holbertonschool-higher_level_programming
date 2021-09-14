#!/usr/bin/python3


def no_c(my_string):

    if my_string is None:
        return(None)

    new_string = my_string.translate({ord('c'): None, ord('C'): None})

    return(new_string)
