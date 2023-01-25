#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size(int): The size of the new square.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Evaluate area of a square.
        Returns:
            The return value is the area of a square.
        """
        return int(self.__size) * int(self.__size)

    @property
    def size(self):
        """Get the size of a square:
        Return: The size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
