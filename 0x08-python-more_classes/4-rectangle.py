#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Defining rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return (('#' * self.width + '\n') * (self.height - 1) + '#' * self.width)

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
