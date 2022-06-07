#!/usr/bin/python3
"""Module"""


import json
import os
import csv


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
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(
                    cls.to_json_string([i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        if os.path.exists(cls.__name__ + ".json") is True:
            with open(cls.__name__ + ".json") as f:
                objs = cls.from_json_string(f.read())
                ret = []
                for i in objs:
                    ret.append(cls.create(**i))
                return ret
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + ".csv", "w", newline="") as csvf:
            w = csv.writer(csvf)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    w.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    w.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        lst = []
        try:
            with open(cls.__name__ + ".csv") as csvf:
                r = csv.reader(csvf)
                for i in r:
                    if cls.__name__ == "Rectangle":
                        dctry = {"id": int(i[0]), "width": int(i[1]),
                                 "height": int(i[2]), "x": int(i[3]),
                                 "y": int(i[4])}
                    elif cls.__name__ == "Square":
                        dctry = {"id": int(i[0]), "size": int(i[1]),
                                 "x": int(i[2]), "y": int(i[3])}
                    obj = cls.create(**dctry)
                    lst.append(obj)
        except Exception:
            pass
        return lst
