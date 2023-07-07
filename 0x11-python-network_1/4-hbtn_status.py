#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

url = " https://alx-intranet.hbtn.io/status"
request = urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    content = response.read().decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
