#!/usr/bin/python3
"""Import a JSON module"""
import json

"""A function that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """JSON representation of my_str
    Return:
        JSON representation
    """
    return json.dumps(my_str)
