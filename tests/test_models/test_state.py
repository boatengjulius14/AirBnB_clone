#!/usr/bin/python3
"""Unittesting for the state module"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Definition of TestState with tests for the State class
    in the state module
    """

    def setUp(self):
        """Set up method for producing and instance of the class
        State
        """
        self.obj = State()

    def test_class(self):
        self.assertTrue(issubclass(type(self.obj), BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.obj, "name"))
        self.assertIs(type(self.obj.name), str)
        self.assertFalse(bool(self.obj.name))


if __name__ == "__main__":
    unittest.main()
