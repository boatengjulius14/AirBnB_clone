#!/usr/bin/python3
"""Unittesting for file_storage module"""
import os
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Definition of TestFileStorage Class"""

    @classmethod
    def setUp(self):
        """setup method for renaming file.json"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """teardown method regenerating file.json"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_class(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_public_fields(self):
        self.assertFalse(hasattr(FileStorage(), "__file_path"))
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_with_args(self):
        self.assertRaises(TypeError, FileStorage, 5)

    def test_storage(self):
        self.assertEqual(type(storage), FileStorage)

    def test_all_method(self):
        self.assertEqual(type(storage.all()), dict)
        self.assertTrue(type(storage.all()) is dict)
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_method(self):
        self.assertIn("BaseModel." + BaseModel().id,
                      storage.all().keys())
        self.assertRaises(TypeError, storage.new, BaseModel(), 5)
        self.assertRaises(AttributeError, storage.new, 5)
        self.assertRaises(TypeError, storage.new)

        obj_bm = BaseModel()
        obj_user = User()
        obj_state = State()
        obj_city = City()
        obj_place = Place()
        obj_review = Review()
        obj_amenity = Amenity()

        self.assertIn("BaseModel." + obj_bm.id,
                      storage.all().keys())
        self.assertIn(obj_bm, storage.all().values())
        self.assertIn("User." + obj_user.id, storage.all().keys())
        self.assertIn(obj_user, storage.all().values())
        self.assertIn("State." + obj_state.id, storage.all().keys())
        self.assertIn(obj_state, storage.all().values())
        self.assertIn("Place." + obj_place.id, storage.all().keys())
        self.assertIn(obj_place, storage.all().values())
        self.assertIn("City." + obj_city.id, storage.all().keys())
        self.assertIn(obj_city, storage.all().values())
        self.assertIn("Amenity." + obj_amenity.id,
                      storage.all().keys())
        self.assertIn(obj_amenity, storage.all().values())
        self.assertIn("Review." + obj_review.id,
                      storage.all().keys())
        self.assertIn(obj_review, storage.all().values())

        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_method(self):
        obj = BaseModel()
        storage.save()

        with open("file.json") as file:
            test_str = file.read()
        self.assertIn("BaseModel." + obj.id, test_str)

        self.assertRaises(TypeError, storage.save, 5)

        obj_bm = BaseModel()
        obj_user = User()
        obj_state = State()
        obj_city = City()
        obj_place = Place()
        obj_review = Review()
        obj_amenity = Amenity()

        storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + obj_bm.id, save_text)
            self.assertIn("User." + obj_user.id, save_text)
            self.assertIn("State." + obj_state.id, save_text)
            self.assertIn("Place." + obj_place.id, save_text)
            self.assertIn("City." + obj_city.id, save_text)
            self.assertIn("Amenity." + obj_amenity.id, save_text)
            self.assertIn("Review." + obj_review.id, save_text)

        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        obj = BaseModel()
        storage.save()

        object_list1 = storage._FileStorage__objects

        self.assertIn("BaseModel." + obj.id, object_list1)
        self.assertRaises(TypeError, storage.reload, 5)

        obj_bm = BaseModel()
        obj_user = User()
        obj_state = State()
        obj_city = City()
        obj_place = Place()
        obj_review = Review()
        obj_amenity = Amenity()

        storage.save()
        storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + obj_bm.id, objects)
        self.assertIn("User." + obj_user.id, objects)
        self.assertIn("State." + obj_state.id, objects)
        self.assertIn("Place." + obj_place.id, objects)
        self.assertIn("City." + obj_city.id, objects)
        self.assertIn("Amenity." + obj_amenity.id, objects)
        self.assertIn("Review." + obj_review.id, objects)

        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
