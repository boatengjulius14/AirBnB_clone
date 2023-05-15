#!/usr/bin/python3
"""Unittesting for the amenity module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Definition of TestAmenity with tests for the Amenity class
    in the amenity module
    """

    def setUp(self):
        """Setup method for producing an instance the class
        Amenity
        """
        self.obj = Amenity()

    def test_class(self):
        self.assertTrue(issubclass(type(self.obj), BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.obj, "name"))
        self.assertIs(type(self.obj.name), str)
        self.assertFalse(bool(self.obj.name))


if __name__ == "__main__":
    unittest.main()
