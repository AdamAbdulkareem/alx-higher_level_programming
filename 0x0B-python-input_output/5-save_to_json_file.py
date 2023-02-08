#!/usr/bin/python3
"""Import a JSON module"""
import json
"""A function that writes an object to a text file using JSON representation"""
def save_to_json_file(my_obj, filename):
    """Write the filename or path provided by the function
    Return:
        Text written to the provided filename or path
    """
    with open(filename, "w", encoding="utf-8") as text_file:
        json_object = json.dumps(my_obj)
        write_file = text_file.write(json_object)
        return write_file
