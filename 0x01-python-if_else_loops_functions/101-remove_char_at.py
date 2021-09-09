#!/usr/bin/python3


def remove_char_at(str, n):

    output = ''

    if n > len(str):
        return (str)

    if n < 0:
        return (str)

    for i in str:
        if i != str[n]:
            output += i

    return (output)
