#!/usr/bin/python3
"""Unittesting for the city module"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Definition of TestCity with tests for the City class
    in the city module
    """

    def setUp(self):
        """Set up method for producing and instance of the class
        State
        """
        self.city = City()

    def test_class(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        self.assertIs(type(self.city.state_id), str)
        self.assertFalse(bool(self.city.state_id))
        self.assertIs(type(self.city.name), str)
        self.assertFalse(bool(self.city.name))


if __name__ == "__main__":
    unittest.main()
