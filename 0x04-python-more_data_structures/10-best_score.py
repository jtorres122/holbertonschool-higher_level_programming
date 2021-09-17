#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return (None)

    flag = 1
    for key in a_dictionary:
        if flag == 1:
            biggestval = a_dictionary[key]
            biggestkey = key
            flag = 0
        if a_dictionary[key] > biggestval:
            biggestval = a_dictionary[key]
            biggestkey = key

    return (biggestkey)
