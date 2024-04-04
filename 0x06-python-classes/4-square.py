#!/usr/bin/python3
"""
This a module 4-square

It contains a class Square that defines a square based on module 3-square by:
    - Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it
            if size is not an integer, raise TypeError with error message
            if size is less than 0, raise ValueError with error message
    - Importing any module is not permitted.
"""


class Square:
    """A class that calculates area of square and use setters and getters."""

    def __init__(self, size=0):
        """
        Instantiates size attribute upon object creation.

        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):         # A public instance method
        return (self.__size ** 2)
