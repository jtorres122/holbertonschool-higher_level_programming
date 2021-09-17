#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    new_dict = {}

    for keys, val in a_dictionary.items():
        total = val * 2
        new_dict.update({keys: total})

    return (new_dict)
