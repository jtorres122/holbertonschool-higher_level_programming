#!/bin/bash
# Bash script sets a header value and displays body
curl -s -X GET -H "X-School-User-Id: 98" "$1"
