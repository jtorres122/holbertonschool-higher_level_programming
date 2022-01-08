#!/bin/bash
# Bash script displays status code of the response
curl -so /dev/null -w '%{http_code}' "$1"
