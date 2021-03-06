#!/usr/bin/python3
"""Module"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dictry = {}
            for i in attrs:
                if type(i) is str:
                    for key, value in self.__dict__.items():
                        if key in attrs:
                            dictry[key] = value
                else:
                    return self.__dict__
            return dictry
        return self.__dict__
