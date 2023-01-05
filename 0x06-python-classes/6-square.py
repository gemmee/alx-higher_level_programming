#!/usr/bin/python3
"""
This is module 6-square

This module contains one class Square
"""


class Square:
    """
    This class Square creates a square from a size

    Fields:
        size: needed for instantiation, private
        position: tuple of 2 ints, also private

    Methods:
        __init__(self, size)
        area(self)
        size(self)
        size(self, value)
        my_print(self)
        position(self)
        position(self, value)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiate a Square object

        Args:
            size: must be a positive or null integer
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute

        No arguments

        Return:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Args:
            value: value to be passed to size, should be an int >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute

        No arguments

        Return:
            the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute

        Args:
            value: tuple of non negative int to be set to position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in ascii art

        No arguments
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            print("\n".join([" " * self.__position[0] + '#' * self.__size
                             for i in range(self.__size)]))
