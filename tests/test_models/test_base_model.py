#!/usr/bin/python3
"""Unittess for the base_model model"""
from datetime import datetime
from models.base_model import BaseModel
import time
import unittest
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """Definition of various tests"""
    def setUp(self):
        """setUp method with self.obj and self.obj1
        being an instance of the BaseModel class
        """
        self.obj = BaseModel()
        time.sleep(0.01)
        self.obj1 = BaseModel()

    def test_cls_obj_and_attr(self):
        self.assertEqual(BaseModel, type(self.obj))
        self.assertTrue(hasattr(self.obj, "id"))
        self.assertNotEqual(self.obj.id, self.obj1.id)
        self.assertEqual(type(self.obj.id), str)

    def test_created_at_and_updated_at(self):
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(type(self.obj.created_at), datetime)
        self.assertLess(self.obj.created_at, self.obj1.created_at)

    def test_str_method(self):
        self.assertEqual(str(self.obj),
                         "[BaseModel] ({}) {}".format(self.obj.id,
                                                      self.obj.__dict__))

    def test_to_dict_method(self):
        self.assertEqual(type(self.obj.to_dict()), dict)
        self.assertEqual(self.obj.to_dict()["updated_at"],
                         self.obj.updated_at.isoformat())
        self.assertEqual(self.obj.to_dict()["created_at"],
                         self.obj.created_at.isoformat())
        self.assertEqual(len(self.obj.__dict__), len(self.obj.to_dict()) - 1)
        self.assertNotEqual(self.obj.to_dict(), self.obj.__dict__)

        attributes = ("id", "created_at", "updated_at", "__class__")
        for key in attributes:
            self.assertIn(key, self.obj.to_dict())

        obj = BaseModel()
        obj.id = "a6a6a6"
        obj.created_at = obj.updated_at = datetime.now()
        _dict = {'id': 'a6a6a6',
                 'created_at': obj.created_at.isoformat(),
                 'updated_at': obj.updated_at.isoformat(),
                 '__class__': 'BaseModel'
                 }
        self.assertDictEqual(obj.to_dict(), _dict)

    def test_args(self):
        obj = BaseModel(5)
        self.assertNotIn(5, obj.__dict__.values())
        self.assertRaises(TypeError, obj.to_dict, None)

    def test_kwargs(self):
        _dict = BaseModel().to_dict()
        obj = BaseModel(**_dict)
        self.assertEqual(obj.id, _dict["id"])
        self.assertEqual(obj.created_at,
                         datetime.strptime(_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(obj.updated_at,
                         datetime.strptime(_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_passing_args_and_kwargs(self):
        time_iso = datetime.now().isoformat()
        obj = BaseModel("Hello", id="b6a6e", created_at=time_iso,
                        name="New Model")
        self.assertEqual(obj.id, "b6a6e")
        self.assertEqual(obj.created_at, datetime.fromisoformat(time_iso))
        self.assertEqual(obj.name, "New Model")

        _dict = {
            "id": uuid4(), "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "New Model"
            }
        obj = BaseModel(**_dict)
        self.assertTrue(hasattr(obj, "name"))
