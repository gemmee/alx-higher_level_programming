#!/usr/bin/python3
"""
This is module 11-square

This module contains one class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class that inherits from Rectangle.

    Fields:
        size: a positive integer
    Methods:
        __init__
        __str__
    """
    def __init__(self, size):
        """Instantiates a square

        Args:
            size: must be a positive int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Makes nice string"""
        return "[{}] {size}/{size}".format(self.__class__.__name__,
                                           size=self.__size)
