#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, op, b = int(argv[1]), argv[2], int(argv[3])
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if op in ops:
        res = ops[op](a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
