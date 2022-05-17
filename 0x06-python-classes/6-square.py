#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defining square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size retriever"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position retriever"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        else:
            position = self.__position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for j in range(self.size):
                print(" " * position[0] + "#" * self.size)
