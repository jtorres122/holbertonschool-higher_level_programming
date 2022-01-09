#!/usr/bin/python3
'''Module fetches a URL's data'''
from requests import get


if __name__ == "__main__":
    
    resp = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
