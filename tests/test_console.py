#!/usr/bin/python3
"""Unittests for console module"""


from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
import os
import sys
import unittest
from unittest.mock import create_autospec, patch


class TestConsole(unittest.TestCase):
    """Definition of tests for HBNBCommand Class"""

    def setUp(self):
        """Setup method"""
        self.stdin = create_autospec(sys.stdin)
        self.stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.stdin, stdout=self.stdout)

    def last_write(self, test=None):
        if test is None:
            return self.stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Quit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))


if __name__ == '__main__':
    unittest.main()
