#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = abs(number) % 10
string1 = "Last digit of "
string2 = "less than 6 and not 0"

if ld == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, ld))
elif ld < 6 and ld != 0:
    print("{:s}{:d} is {:d} and {:s}".format(string1, number, ld, string2))
else:
    print("{:s}{:d} is {:d} and is greater than 5".format(string1, number, ld))
