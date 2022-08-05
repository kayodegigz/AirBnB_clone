#!/usr/bin/python3
"""
JSON instantiation class
"""

import json
from models.user import User

class FileStorage:
    __file_path = ""
    __objects = {}

    def save(self):
        """
        manage serialization of objects to json
        """
        new_obj = {}

        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_obj, file)

