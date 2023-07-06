#!/bin/bash
# Script that takes in a URL and display all HTTP methods the server will accept
curl -s -X OPTIONS -i "$1" | awk -F ": " '/^(Allow|Access-Control-Allow-Methods):/ {print $2}'
