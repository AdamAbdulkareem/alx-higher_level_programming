#!/usr/bin/python3
"""Import a JSON module"""
import json

"""A function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """JSON representation of my_obj
    Return:
        JSON representation
    """
    return json.dumps(my_obj)
