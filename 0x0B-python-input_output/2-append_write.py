#!/usr/bin/python3
"""A function that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """Append text at the provided filename or path
    Return:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as append_file:
        return append_file.write(text)
