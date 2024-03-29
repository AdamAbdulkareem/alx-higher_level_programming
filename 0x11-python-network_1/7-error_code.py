#!/usr/bin/python3
"""
This script takes in a URL sends a request to the URL,
and displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status_code = response.status_code

    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(f"{response.text}")
