#!/usr/bin/python3
"""
Module contains the base class that every other class will
inherit from
"""
from datetime import datetime
from uuid import uuid4


class BaseModel ():
    def __init__(self, *args, **kwargs):
        """initialises instance attribute values"""
        if kwargs:
            for key, value in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns the specified string representation"""
        return "[{}] ({}) {}".format(__class__.name, self.id, self.__dict__)

    def save(self):
        """changes the updated_at time so we know when last the instance was modified"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary representation of all attrs and the class name"""
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value

        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__

        return new_dict
