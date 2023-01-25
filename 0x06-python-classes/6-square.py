#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size(int): The size of the new square.
        """
        self.__size = size
        self.__position = position
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
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Print the square in stdout with the character #.
        Returns:
            Print the square.
        """
        if self.__size == 0:
            print()
            return
        square_value = int(self.__size)
        square_display = "#" * square_value
        for n in range(0, int(self.__size)):
            print(square_display, end="\n")
        return

    @property
    def position(self):
        """Get the position of a square:
        Return: The position of a square
        """
        return self.__postion

    @position.setter
    def postion(self, value):
        """Set the position of a square"""
        self.__position = value
        if len(value) > 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
