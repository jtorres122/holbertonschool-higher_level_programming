#!/usr/bin/python3
'''Module fetches a URL's data'''
from requests import get


if __name__ == "__main__":
    with get('https://intranet.hbtn.io/status') as resp:
        print("Body response:")
        print("    - type: {}".format(type(resp.text)))
        print("    - content: {}".format(resp.text))
