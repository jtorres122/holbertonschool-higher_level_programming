#!/bin/bash
# Bash script displays takes a URL, sends a request and displays the size of body of response
curl -so /dev/null "$1" -w '%{size_download}'
