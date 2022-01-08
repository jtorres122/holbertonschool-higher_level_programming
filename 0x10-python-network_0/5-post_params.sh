#!/bin/bash
# Bash script POST two variables
curl -s -X POST -d email='test@gmail.com' -d subject='I will always be here for PLD' "$1"
