#!/bin/bash
# Bash script sends a JSON POST request and displays the response
curl -s -X POST -d @"$2" "$1"
