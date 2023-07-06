#!/usr/bin/python3
from urllib.request import urlopen
with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
