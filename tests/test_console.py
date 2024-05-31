#!/usr/bin/python3
"""
This module contains unit tests for the HBNBCommand class in the console\
    module.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User


class TestCreateCommand(unittest.TestCase):
    """
    This class contains unit tests for the create command in the HBNBCommand\
        class.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of the HBNBCommand\
            class.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up the test environment by deleting the instance of the\
            HBNBCommand class.
        """
        pass

    @patch("sys.stdout", new_callable=StringIO)
    def test_create(self, mock_stdout):
        """
        Test the create command in the HBNBCommand class.

        This test case checks if the create command generates a valid UUID
        when creating instances of BaseModel and User classes.
        """
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(len(output), 36)

        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(len(output), 36)


if __name__ == "__main__":
    unittest.main()
