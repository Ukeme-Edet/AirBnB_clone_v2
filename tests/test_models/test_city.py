#!/usr/bin/python3
"""
This module contains unit tests for the City class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    This class contains unit tests for the City class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            name (str): The name of the city.
            value (City): The City class itself.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test case to verify the type of the state_id attribute in the City class.

        It creates a new instance of the City class using the value() method,
        and then asserts that the type of the state_id attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test case to verify the type of the 'name' attribute of a City instance.

        It creates a new City instance using the 'value' method from the test class.
        Then, it asserts that the type of the 'name' attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
