#!/usr/bin/python3
'''Module fetches a URL's data'''
import requests
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    req = requests.post(argv[1], email)
    print(req.text)
