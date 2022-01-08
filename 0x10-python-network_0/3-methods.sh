#!/bin/bash
# Bash script displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -i | grep "Allow" | cut -d ' ' -f 2-
