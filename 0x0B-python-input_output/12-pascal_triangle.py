#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    plist = []
    if n <= 0:
        return plist
