#!/usr/bin/python3
"""
This module contains the unit tests for the State class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    This class contains the unit tests for the State class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the test_state class.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test case to check the type of the 'name' attribute of a new State\
            instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
