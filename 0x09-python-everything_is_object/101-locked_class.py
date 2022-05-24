#!/usr/bin/python3
"""Module"""


class LockedClass:
    """Class"""
    __slots__ = ['first_name']

    def __init__(self, value=''):
        """Init"""
        self.first_name = value
