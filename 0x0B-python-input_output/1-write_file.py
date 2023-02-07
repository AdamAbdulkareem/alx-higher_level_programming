#!/usr/bin/python3
"""A function that writes a string to a text file and returns the number of character"""


def write_file(filename="", text=""):
    """Write to file at the provided filename or path"""
    with open(filename, "w", encoding="utf-8") as text_file:
        write_text = text_file.write(text)
        return write_text
