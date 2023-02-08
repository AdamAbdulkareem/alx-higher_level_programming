#!/usr/bin/python3
"""Import a JSON module"""
import json

"""A function that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """Convert a JSON string to an object
    Return:
        An object from JSON representation
    """
    return json.loads(my_str)
