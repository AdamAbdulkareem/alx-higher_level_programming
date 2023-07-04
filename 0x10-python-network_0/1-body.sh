#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL and 
# displays the body of the response,
url="$1"
response=$(curl -s -w "%{http_code}" "$url")
status_code=${response:(-3)}
body=${response:0:(-3)}

if [[ "$status_code" -eq 200 ]]; then
	echo "$body"
fi
