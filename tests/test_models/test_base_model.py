#!/usr/bin/python3
"""Unittess for the base_model model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Definition of various tests"""
    def setUp(self):
        """setUp method with self.obj being
        an instance of the BaseModel class
        """
        self.obj = BaseModel()

    def test_equals(self):
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.to_dict()["updated_at"],
                         self.obj.updated_at.isoformat())
        self.assertEqual(str(self.obj),
                         "[BaseModel] ({}) {}".format(self.obj.id,
                                                      self.obj.__dict__))
        self.assertEqual(self.obj.to_dict()["created_at"],
                         self.obj.created_at.isoformat())
