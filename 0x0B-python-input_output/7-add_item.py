#!/usr/bin/python3
"""Import a SYS module"""
import sys
"""Import a JSON module"""
import json

"""A function that creates an object from a JSON file"""


def load_from_json_file(filename):
    """Create Object from provided filename or path"""
    with open(filename, encoding="utf-8") as json_file:
        display_file = json_file.read()
        create_obj = json.loads(display_file)
        return create_obj


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


for items in range(1, len(sys.argv)):
    display_argv = sys.argv[items]
    display_list = load_from_json_file("add_item.json")
    append_display_list = display_list.append(display_argv)
    save_to_json_file(append_display_list, "add_item.json")
