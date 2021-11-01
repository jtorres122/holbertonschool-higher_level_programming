#!/usr/bin/python3
'''Module contains function that adds args to a list and saves them to a file'''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

filename = "add_item.json"
del sys.argv[0]
save_to_json_file(sys.argv, filename)
