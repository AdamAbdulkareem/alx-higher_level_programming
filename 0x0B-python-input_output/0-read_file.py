#!/usr/bin/python3
"""A function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Read file with provided filename or path"""
    with open(filename, encoding="utf-8") as text_file:
        read_file = text_file.read()
        print(read_file, end="")
        return
