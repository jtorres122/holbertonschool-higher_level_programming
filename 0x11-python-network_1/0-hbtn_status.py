#!/usr/bin/python3
'''Module fetches a URL's info'''
from urllib import request
import urllib


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        info = response.read()
        print("Body response:")
        print("    - type: {}".format(type(info)))
        print("    - content: {}".format(info))
        print("    - utf8 content: {}".format(info.decode('utf8')))
