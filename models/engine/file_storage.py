#!/usr/bin/python3
"""
JSON instantiation class
"""

import json
import os
from models.user import User


class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        if obj:
            obj_dict_key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[obj_dict_key] = obj

    def save(self):
        """
        manage serialization of objects to json
        """
        new_obj = {}

        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        """"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    """value is a dict, __class__ contains the class name
                    but it's a str, it can't be used as a str so
                    I used eval to strip the str off"""
                    cls_name = eval(value['__class__'])
                    """initialises an instance like class(**kwargs), (check
                    init method of BaseModel) then passes the instance(object)
                    to the 'new' method so it can be added to the __objects
                    dictionary"""
                    self.__objects[key] = cls_name(**value)
        else:
            return
