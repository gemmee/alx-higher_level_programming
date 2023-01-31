#!/usr/bin/python3
"""
This is module 5-rectangle
This module contains 1 class Rectangle
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
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
    """

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle.
        Args:
            width: facultative, a non-negative int
            height: facultative, a non-negative int
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter of Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
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

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Rectangle width
        Args:
            value: non negative int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """String representation of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        """Repr of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete instance"""
        print("Bye rectangle...")
