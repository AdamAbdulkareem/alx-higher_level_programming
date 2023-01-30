#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new instance of a rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
        return

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return