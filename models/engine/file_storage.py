#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {key: obj.to_dict() for key, obj in type(self).__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    obj = eval(class_name)(**val)
                    type(self).__objects[key] = obj
        except FileNotFoundError:
            pass

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        from models.amenity import Amenity

        amenity_instances = []
        for amenity_id in self.amenity_ids:
            key = "Amenity." + amenity_id
            amenity_instance = self.__objects.get(key)
            if amenity_instance and isinstance(amenity_instance, Amenity):
                amenity_instances.append(amenity_instance)
        return amenity_instances

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for amenities"""
        if isinstance(obj, Amenity):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
        if key in self.__objects:
            del self.__objects[key]
