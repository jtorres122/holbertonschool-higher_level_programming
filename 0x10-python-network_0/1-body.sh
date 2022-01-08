#!/bin/bash
# Bash script takes a URL, sends a GET request and displays the body of response
curl -s -X GET "$1"
