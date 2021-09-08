#!/usr/bin/env python3


def uppercase(str):

    output = ''

    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            k = ord(n) - 32
            output = output + chr(k)
        else:
            output = output + n

    print("{:s}".format(output))
