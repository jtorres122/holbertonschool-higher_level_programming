#!/bin/bash
# Bash script POST two variables
curl -so /dev/null -w '%{http_code}' "$1"
