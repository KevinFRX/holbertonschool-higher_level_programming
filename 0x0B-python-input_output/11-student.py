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
            for i in attrs:
                if type(i) is str:
                    dictry = {}
                    for key, value in self.__dict__.items():
                        if key in attrs:
                            dictry[key] = value
                    return dictry
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__.update({i: json[i]})
