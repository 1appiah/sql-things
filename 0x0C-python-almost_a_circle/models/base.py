#!/usr/bin/python3
"""this is the base class"""


import json


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json repre"""
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json repr of listobjs to a file"""
        with open("{}.json".format(cls), "w", encoding="UTF-8") as f:
            f.write(Base.to_json_string(list_objs))