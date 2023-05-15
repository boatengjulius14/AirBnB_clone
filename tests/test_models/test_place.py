#!/usr/bin/python3
"""Unittesting for the place module"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Definition of TestPlace with tests for the Place class
    in the place module
    """

    def setUp(self):
        """SetUp method"""
        self.obj = Place()
        self.attr_list = ["city_id", "user_id", "name", "description",
                          "number_rooms", "number_bathrooms", "max_guest",
                          "price_by_night", "latitude", "longitude",
                          ]

    def test_class(self):
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(type(self.obj), BaseModel))

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.obj, attr)))

        string_list = ["city_id", "user_id", "name", "description",
                       "amenity_ids"]
        int_list = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        float_list = ["latitude", "longitude"]
        for attr in string_list:
            self.assertTrue(type(getattr(self.obj, attr)), str)
        for attr in int_list:
            self.assertTrue(type(getattr(self.obj, attr)), int)
        for attr in float_list:
            self.assertTrue(type(getattr(self.obj, attr)), float)


if __name__ == "__main__":
    unittest.main()
