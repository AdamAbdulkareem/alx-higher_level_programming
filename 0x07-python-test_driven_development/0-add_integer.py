#!/usr/bin/python3
"""Addition module 
Args:
    param1 (int): The first parameter
    param2 (int): Preset parameter
"""
def add_integer(a, b=98):
    """A function that adds 2 integer
    Returns: The addition of 2 integers
    """
    if (type(a) != int and type(a) == float):
        a = int(a)
    if (type(b) != int and type(b) == float):
        b = int(b)
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return a + b
