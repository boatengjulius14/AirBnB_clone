#!/usr/bin/python3
"""Unittesting for User Class in User module"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Definition of TestUser with all tests for
    User Class"""
    def setUp(self):
        """setUp method for creating and instance
        of the class User"""
        self.obj = User()

    def test_class(self):
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(self.obj), User))

    def test_class_attributes(self):
        self.assertTrue(hasattr(self.obj, "email"))
        self.assertTrue(hasattr(self.obj, "password"))
        self.assertTrue(hasattr(self.obj, "first_name"))
        self.assertTrue(hasattr(self.obj, "last_name"))

    def test_data_types(self):
        self.assertIs(type(self.obj.email), str)
        self.assertIs(type(self.obj.password), str)
        self.assertIs(type(self.obj.first_name), str)
        self.assertIs(type(self.obj.last_name), str)

    def test_attr_values(self):
        self.assertEqual(self.obj.email, "")
        self.assertEqual(self.obj.password, "")
        self.assertEqual(self.obj.first_name, "")
        self.assertEqual(self.obj.last_name, "")


if __name__ == "__main__":
    unittest.main()
