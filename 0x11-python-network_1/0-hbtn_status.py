#!/usr/bin/python3
"""
This script retrieves the content of a URL and print various details about the response
"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")
