#!/bin/bash
# Bash script displays takes a URL, sends a request and displays the size of body of response
curl -so /dev/null 0.0.0.0:5000 -w '%{size_download}'
