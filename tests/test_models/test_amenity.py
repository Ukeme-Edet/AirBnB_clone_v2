#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    This class contains unit tests for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test case to verify the type of the 'name' attribute of an Amenity\
            instance.

        It creates a new instance of the Amenity class using the 'value'\
            method,
        and then asserts that the type of the 'name' attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
