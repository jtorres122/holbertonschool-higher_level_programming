#!/usr/bin/python3
'''Module fetches a URL's data'''
from requests import get


if __name__ == "__main__":
    resp = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("    - type: {}".format(type(resp.text)))
    print("    - content: {}".format(resp.text))
