#!/usr/bin/python3
"""
This a module 3-square

It contains a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0):
        @ size: must be an integer, otherwise TypeError is raised with a
          message 'size must be an integer'
        @ if size is less than 0, a ValueError is raised with the message
          'size must be >= 0'
    - Public instance method: def area(self): that returns the current area
    - Importing any module is not permitted.
"""


class Square:
    """
    A class with private instance attribute size and public instance method

    """
    def __init__(self, size=0):
        """
        Instantiation with size which is optional

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size ** 2)
