#!/usr/bin/python3
"""
This script takes in a URL,sends a request to the URL
and displays the body of the response(decoded in UTF-8)
"""

import sys
import urllib.request
import urllib.error

url = sys.argv[1]
request = urllib.request.Request(url)
try:
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
