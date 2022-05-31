#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
