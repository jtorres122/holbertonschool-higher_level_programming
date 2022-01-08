#!/bin/bash
# Bash script takes a URL, sends a DELETE request and displays the body of response
curl -s -X DELETE "$1"
