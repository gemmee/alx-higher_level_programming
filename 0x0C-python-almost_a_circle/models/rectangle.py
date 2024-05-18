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

    def area(self):
        """Returns the area of a Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with a character #
        """
        print("\n" * self.y, end="")
        print("\n".join([' ' * self.x + '#' * self.__width for
              i in range(self.__height)]))

    def __str__(self):
        """Returns the string representation of the object
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Assigns key/value argument to attributes

        Args:
            *args: variable number of no-keyword args
            *kwargs: variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns the dictionary repr of a rectance
        """
        return {'x': getattr(self, 'x'), 'y': getattr(self, 'y'),
                'id': getattr(self, 'id'), 'height': getattr(self, 'height'),
                'width': getattr(self, 'width')}
