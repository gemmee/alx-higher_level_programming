#!/usr/bin/python3
"""
This is module 1-rectangle

It contains 1 class rectangle.
"""


class Rectangle:
    """Defines class Rectangle

    Instance fields:
        width: private must be a non negative int
        height: private must be a non negative int

    Instance methods:
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        __init__(self, width=0, height=0)
        __check_arg(self, value)

    """
    def __init__(self, width=0, height=0):
        """A constructor that inistantiates a Rectangle.

        Args:
            width: facultative, a non-negative int
            height: facultative, a non-negative int
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter, retrieves height."""
        return height.__return

    @height.setter
    def height(self, value):
        """Setter for rectangle height.

        Args:
            value: non-negative int

        Raise:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise TypeError("{} must be an integer".format(value))
        self.__height = value

    @property
    def width(self):
        """Getter, retrieves width."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for rectangle width.

        Args:
            value: non-negative int

        Raise:
            TypeError: If the width is not an integer
            ValueError: If the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise TypeError("{} must be an integer".format(value))
        self.__width = value
