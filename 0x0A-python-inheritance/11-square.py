#!/usr/bin/python3
"""
This is a 11-square module

It contains one class Square that inherits from Rectangle class that
is in 9-rectangle module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes the Square
        Args:
            size (int): private and must be positive
        """
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
