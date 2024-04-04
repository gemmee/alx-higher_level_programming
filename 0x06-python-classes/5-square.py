#!/usr/bin/python3
"""
This is module 5-square

This module contains a class Square that defines a square based on module
4-square by:
    * Private instance attribute: size:
        @property def size(self): to retrieve it
        @property setter def size(self, value): to set it:
            -size must must be an integer, otherwise exception is raised.
            -size must not be less than 0, otherwise exception is raised.
    * Instantiation with optional size: def __init__(self, size=0):
    * Public instance method: def area(self): that returns the area of square
    * Public instance method: def my_print(self):
    * Importing any module is not allowed.
"""


class Square:
    """
    This class square creates a square from a size

    **fields**
    size: needed for instantiation, hidden

    **methods**
    __init__(self, size)
    area(self)
    size(self)
    size(self, value)
    my_print(self)

    """
    def __init__(self, size=0):
        """
        Instantiate a Square object

        Args:
            size: must be a positive or null integer
        """
        self.size = size

    def area(self):
        """
        Computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        A getter(accessor) method for the size attribute

        No arguments

        Return:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for the size attribute

        Args:
            value: value to be passed as size, should be int >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square in ascii art

        No arguments
        """
        print("\n".join(["#" * self.__size for i in range(self.__size)]))
