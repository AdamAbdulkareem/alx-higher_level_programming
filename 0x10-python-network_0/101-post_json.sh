#!/bin/bash
# Script that sends a JSON post request to a URL passed as the first argument and display the body of the response
file_content=$(cat "$2")
curl -sX POST -H "Content-Type: application/json" -d "$file_content" "$1"
