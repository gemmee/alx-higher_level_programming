#!/usr/bin/python3
"""This is module 101-square

This module contains one class Square
"""


class Square:
    """This class Square creates a square from a size

    Fields:
        size: needed for instantiation, private
        position: tuple of 2 ints, private

    Methods:
        __init__(self, size)
        area(self)
        size(self)
        size(self, value)
        my_print(self)
        position(self)
        position(self, value)
        __str__(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a Square object

        Args:
            size: must be a positive or null integer
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute

        No arguments

        Return:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute

        Args:
            value: value to be passed to size, should be an int >= 0

        Raises:
            TypeError: If size is not an integer value
            ValueError: If size is less than 0
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute

        No arguments

        Return:
            the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute

        Args:
            value: tuple of non negative int to be set to position

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of a square of a given size

        No arguments

        Returns:
            area of square (int)
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square in ascii art

        No arguments
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)]))

    def __str__(self):
        """String format for print

        No arguments
        """
        if self.__size == 0:
            return ""
        string = "\n" * self.__position[1]
        string += "\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)])
        return string
