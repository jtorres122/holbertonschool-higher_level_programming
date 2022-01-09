#!/usr/bin/python3
'''Module fetches a URL's data'''
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print("{}".format(resp.getheader('X-Request-Id')))
