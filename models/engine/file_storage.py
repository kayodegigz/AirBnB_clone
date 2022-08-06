#!/usr/bin/python3
"""
JSON instantiation class
"""

import json
import os
from models.user import User

class FileStorage:
    """"""
    __file_path = ""
    __objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        obj_dict_key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[obj_dict_key] = self.__dict__

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
                

        else:
            return
