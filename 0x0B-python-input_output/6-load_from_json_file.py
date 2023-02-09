#!/usr/bin/python3
"""Import a JSON module"""
import json

"""A function that creates an object from a JSON file"""


def load_from_json_file(filename):
    """Create Object from provided filename or path"""
    with open(filename, encoding="utf-8") as json_file:
        display_file = json_file.read()
        create_obj = json.loads(display_file)
        return create_obj
