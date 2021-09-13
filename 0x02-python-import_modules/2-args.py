#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv) - 1

    if argv == 0:
        print("{:d} arguments.".format(argv))
    elif argv == 1:
        print("{:d} argument:".format(argv))
    else:
        print("{:d} arguments:".format(argv))

    for idx, av in enumerate(sys.argv[1:], 1):
        print("{:d}: {:s}".format(idx, av))
