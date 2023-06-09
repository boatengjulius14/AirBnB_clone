#!/usr/bin/python3
"""Defines the FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Definition of FileStorage Class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with the key
        <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file
        (path: __file_path)
        """
        with open(self.__file_path, "w") as file:
            temp_dict = {}
            for key, obj in self.__objects.items():
                temp_dict[key] = obj.to_dict()
            json.dump(temp_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                for obj in json.load(file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
