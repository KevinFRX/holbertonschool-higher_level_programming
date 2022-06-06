#!/usr/bin/python3
"""Module"""


import json


class Base:
    """First class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
         with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(
                cls.to_json_string([elem.to_dictionary() for elem in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
