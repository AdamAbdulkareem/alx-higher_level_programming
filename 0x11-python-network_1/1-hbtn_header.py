#!/usr/bin/python3
"""This script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""
import sys

if __name__ == "__main__":
    import urllib.request
    
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader("X-Request-Id")

print(x_request_id)