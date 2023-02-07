#!/usr/bin/python3
"""A function that writes a string to a text file and returns the number of character"""


def write_file(filename="", text=""):
    """Write to file at the provided filename or path
    Return:
        The number of characters written"""
    with open(filename, "w", encoding="utf-8") as text_file:
        return text_file.write(text)
