#!/usr/bin/python3
import json
"""Import a JSON module"""
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as text_file:
        json_object = json.dumps(my_obj)
        write_file = text_file.write(json_object)
        return write_file
