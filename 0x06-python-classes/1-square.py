#!/usr/bin/python3
"""
This is module 1-square

It contains one class Square that defines a square by:
    * Private instance attribute: size
    * Instantiation with size (no type/value verification)
    * Importing any module is not allowed
"""


class Square:
    """
    Empty class with private object attribute called size.

    """
    def __init__(self, size):
        """Instantiation with size

        Args:
            size: size of the square
        """
        self.__size = size
