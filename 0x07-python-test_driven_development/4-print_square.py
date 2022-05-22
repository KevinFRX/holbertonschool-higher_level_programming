#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """
    Function that prints a square with the character '#'
    or returns a TypeError if size is not an integer
    or a ValueError if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()
