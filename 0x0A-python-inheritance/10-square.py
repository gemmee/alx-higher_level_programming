#!/usr/bin/python3
"""
This is module 10-square
This module contains one class that inherits from another module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class which is a subclass of Rectangle.

    Fields:
        size: a positive integer, private
    Methods:
        __init__
    """

    def __init__(self, size):
        """Instantiates a square

        Args:
            size: must be a positive int and private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
