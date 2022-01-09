#!/usr/bin/python3
'''Module fetches a URL's data'''
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
