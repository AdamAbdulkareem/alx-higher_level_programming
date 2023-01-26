#!/usr/bin/python3
def add_integer(a, b=98):
    """A function that adds 2 integer"""
    if (type(a) != "int" or "float"):
        raise TypeError("a must be an integer")
    if (type(b) != "int" or "float"):
        raise TypeError("b must be an integer")
    cast_int(a) = int(a)
    cast_int(b) = int(b)
    return cast_int(a) + cast_int(b) 
