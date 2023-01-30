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

    def area(self):
        """Returns the area of a rectangle"""
        area_value = self.__width * self.__height
        return area_value

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        width_value = int(self.__width)
        height_value = int(self.__height)
        perimeter_value = 2 * (width_value + height_value)
        return perimeter_value
