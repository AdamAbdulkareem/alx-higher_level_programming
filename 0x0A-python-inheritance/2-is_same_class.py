#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    check_class = isinstance(obj, a_class)
    if check_class:
        return True
    else:
        return False
