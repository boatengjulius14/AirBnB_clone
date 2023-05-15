#!/usr/bin/python3
"""Base Class Module"""
import uuid
from datetime import datetime


class BaseModel:
    """Definition of BaseModel"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns an informal string representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute 'update_at' with the current
        datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """updates the attribute 'update_at' with the current
        datetime
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                dictionary[key] = value
        return dictionary
