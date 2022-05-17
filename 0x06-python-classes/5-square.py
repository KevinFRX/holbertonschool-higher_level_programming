#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defining square"""
    def __init__(self, size=0):
        """Initialization"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    @property
    def size(self):
        """Retriever"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
