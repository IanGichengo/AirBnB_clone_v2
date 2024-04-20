#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return type(self).__objects
        else:
            return {key: obj for key, obj in type(self).__objects.items()
                    if isinstance(obj, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(type(self).__file_path, 'w') as f:
            temp = {}
            temp.update(type(self).__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(type(self).__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    obj = eval(class_name)(**val)
                    type(self).__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
