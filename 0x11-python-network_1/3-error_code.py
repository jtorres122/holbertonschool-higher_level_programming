#!/usr/bin/python3
'''Module fetches a URL's data'''
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as resp:
            data = resp.read()
            print("{}".format(data.decode('UTF-8')))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
