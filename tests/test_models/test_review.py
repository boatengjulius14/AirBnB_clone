#!/usr/bin/python3
"""Unittesting for the review module"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Definition of TestReview with tests for the Review class
    in the review module
    """

    def setUp(self):
        """Setup method"""
        self.review = Review()
        self.attr_list = ["place_id", "user_id", "text"]

    def test_class(self):
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))


if __name__ == "__main__":
    unittest.main()
