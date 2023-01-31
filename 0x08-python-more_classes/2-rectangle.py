#!/usr/bin/python3
"""
This module defines a class Rectangle.

"""


class Rectangle:
    """ Class that defines a Rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: optional, rectangle width
            height: optional, rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of the rectangle

        Returns:
            rectangle area

        """
        return self.width * self.height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle

        Returns:
            rectangle perimeter

        """
        if (self.width == 0) or (self.height == 0):
            return (0)
        return 2 * (self.width + self.height)
