#!/bin/bash
# Bash script displays all HTTP methods the server will accept
curl -s "$1" -I | grep -Fi Allow
