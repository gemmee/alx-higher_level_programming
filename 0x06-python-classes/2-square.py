#!/usr/bin/python3
"""
This is module 2-square

It contains a class Square that defines a square by:
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        * size must be an integer, otherwise raise a TypeError exception with
        the message size must be an integer
        * if size is less than 0, raise a ValueError exception with the message
        size must be >= 0
    Importing any module is not permitted.
"""


class Square:
    """
    A class with a private instance attribute size and verifies type and
    value of size.

    """
    def __init__(self, size=0):
        """
        Instantiation with optional size.

        Args:
            size: size of the square wich must be an integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
