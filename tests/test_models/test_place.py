#!/usr/bin/python3
"""
This module contains the unit tests for the Place class in the models module.
"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    This class contains the unit tests for the Place class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the test_Place class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test case for the city_id attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test case for the user_id attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Test case for the name attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test case for the description attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Test case for the number_rooms attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Test case for the number_bathrooms attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test case for the max_guest attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Test case for the price_by_night attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Test case for the latitude attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test case for the longitude attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Test case for the amenity_ids attribute of the Place class.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
