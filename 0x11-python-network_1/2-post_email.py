#!/usr/bin/python3
'''Module fetches a URL's data'''
from sys import argv
from urllib import request
from urllib import parse


if __name__ == "__main__":
    email = {"email": argv[2]}
    req = request.Request(argv[1], parse.urlencode(email).encode('UTF-8'))
    with request.urlopen(req) as resp:
        data = resp.read()
        print("{}".format(data.decode('UTF-8')))
