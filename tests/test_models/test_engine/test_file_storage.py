#!/usr/bin/python3
"""Unittesting for file_storage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Definition of TestFileStorage Class"""
    def setUp(self):
        if os.path.exists("file.json"):
            os.rename("file.json", "temp")

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("temp"):
            os.rename("temp", "file.json")

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

    def test_new_method(self):
        self.assertIn("BaseModel." + BaseModel().id,
                      storage.all().keys())
        self.assertRaises(TypeError, storage.new, BaseModel(), 5)
        self.assertRaises(AttributeError, storage.new, 5)
        self.assertRaises(TypeError, storage.new)

    def test_save_method(self):
        obj = BaseModel()
        storage.save()

        with open("file.json") as file:
            test_str = file.read()
        self.assertIn("BaseModel." + obj.id, test_str)

        self.assertRaises(TypeError, storage.save, 5)

    def test_reload_method(self):
        obj = BaseModel()
        storage.save()

        object_list1 = storage._FileStorage__objects

        self.assertIn("BaseModel." + obj.id, object_list1)
        self.assertRaises(TypeError, storage.reload, 5)


if __name__ == "__main__":
    unittest.main()
