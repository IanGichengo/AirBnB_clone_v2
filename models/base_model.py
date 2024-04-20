#!/usr/bin/python3
"""Define The Base Class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The main class for the project
    all other classes will inherant from it."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Attributes:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance."""
        todict = datetime.isoformat
        todict = self.__dict__.copy()
        todict["created_at"] = self.created_at.isoformat()
        todict["updated_at"] = self.updated_at.isoformat()
        todict["__class__"] = self.__class__.__name__
        return todict
