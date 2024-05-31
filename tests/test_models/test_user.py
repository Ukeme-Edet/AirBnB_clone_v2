#!/usr/bin/python3
"""
This module contains unit tests for the User class in the models.user module.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    This class contains unit tests for the User class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a test_User object.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test case to check the type of the first_name attribute.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test case to check the type of the last_name attribute.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test case to check the type of the email attribute.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test case to check the type of the password attribute.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
