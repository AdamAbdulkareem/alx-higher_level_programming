#!/usr/bin/python3
def lookup(obj):
    """A function that print the list of attributes and methods of an object
    Args:
        obj (class): The class object
    Return: List of atrributes and methods
    """
    return dir(obj)
