#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = abs(number) % 10

print("Last digit of {:d} is {:d}".format(number, ld), end='')

if ld == 0:
    print(" and is 0")
elif ld < 6 and ld != 0:
    print(" and is less than 6 and not 0")
else:
   print(" and is greater than 5")
