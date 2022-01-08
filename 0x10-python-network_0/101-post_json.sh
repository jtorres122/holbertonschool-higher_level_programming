#!/bin/bash
# Bash script sends a JSON POST request and displays the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
