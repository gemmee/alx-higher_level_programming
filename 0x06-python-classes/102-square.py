#!/usr/bin/python3
"""This is module 102-square

This module contains one class Square
"""


class Square:
    """This class Square creates a square from a size

    Fields:
        size: needed for instantiation, private

    Methods:
        __init__(self, size)
        area(self)
        size(self)
        size(self, value)
        __lt__(self, other)
        __le__(self, other)
        __eq__(self, other)
        __ne__(self, other)
        __ge__(self, other)
        __gt__(self, other)
    """

    def __init__(self, size=0):
        """Instantiates a Square object

        Args:
            size: must be a positive or null integer
        """
        self.size = size

    def area(self):
        """Computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for the size attribute

        No arguments

        Returns:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute

        Args:
            value: value to be passed to size, should be an int >= 0
        """
        if not type(value) in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Override ==

        Args:
            other: other instance of Square

        Returns:
           True if the squares have same area, False otherwise
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """Override !=

        Args:
            other: other instance of Square

        Returns:
           False if the squares have same area, True otherwise
        """
        return (self.area() != other.area())

    def __gt__(self, other):
        """Override >

        Args:
            other: other instance of Square

        Returns:
           True if self has larger area than other
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """Override >=

        Args:
            other: other instance of Square

        Returns:
           True if self has larger or same area
        """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Override <

        Args:
            other: other instance of Square

        Returns:
           True if self has smallest area
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """Override <=

        Args:
            other: other instance of Square

        Returns:
           True if self has smaller or equal area
        """
        return (self.area() <= other.area())
