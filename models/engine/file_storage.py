import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """to serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects or a filtered dictionary based on the class type"""
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        objects_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as f:
                objects_dict = json.load(f)
                for k, v in objects_dict.items():
                    class_name = k.split(".")[0]
                    self.new(eval(class_name).from_dict(v))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from __objects if it’s inside"""
        if obj is not None and obj in self.__objects.values():
            for k, v in self.__objects.items():
                if v == obj:
                    del self.__objects[k]