#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle implements Base.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance of the class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width.

        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height.

        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for x.

        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for y

        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
