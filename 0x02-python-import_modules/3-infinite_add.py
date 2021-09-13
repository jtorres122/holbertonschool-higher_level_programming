#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total = 0

    for idx in range(len(argv) - 1):
        total += int(argv[idx + 1])

    print("{:d}".format(total))
