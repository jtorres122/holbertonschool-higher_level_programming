#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list is None or len(my_list) == 0:
        return 0

    total = 0
    weight = 0
    for i in my_list:
        total += (i[0] * i[1])
        weight += i[1]

    avg = total / weight

    return avg
