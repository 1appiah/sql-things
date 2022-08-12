#!/usr/bin/python3
"""this is the base class"""

import models
import json
import os


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
        with open("{}.json".format(cls.__name__), "w", encoding="UTF-8") as f:
            thislist = []
            if list_objs is not None:
                for i in list_objs:
                    thislist.append(i.to_dictionary())
            f.write(Base.to_json_string(thislist))

    @staticmethod
    def from_json_string(json_string):
        """converts json string to py object"""
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        inst = ""
        if cls.__name__ == "Rectangle":
            inst = models.rectangle.Rectangle(1, 1)
        else:
            inst = models.square.Square(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """load from from file"""
        f = "{}.json".format(cls.__name__)
        if not os.path.exists(f):
            return []
        string = ""
        with open(f, "r", encoding="UTF-8") as f:
            string = Base.from_json_string(f.read())
        listinst = []
        for i in string:
            if cls.__name__ == "Rectangle":
                listinst.append(models.rectangle.Rectangle.create(**i))
            else:
                listinst.append(models.square.Square.create(**i))
        return listinst
