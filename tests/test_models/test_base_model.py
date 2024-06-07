#!/usr/bin/python3
"""
This module contains the unit tests for the BaseModel class.

The BaseModel class is the base class for all other classes in the project.
It defines common attributes and methods that are inherited by other classes.
These unit tests ensure that the BaseModel class functions as expected.
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from models import storage


class test_basemodel(unittest.TestCase):
    """Test case for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Constructor for the test case."""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Set up method that runs before each test."""
        pass

    def tearDown(self):
        """Tear down method that runs after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test the default behavior of creating an instance of BaseModel."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test creating an instance of BaseModel using keyword arguments."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertNotEqual(i, new)

    def test_kwargs_int(self):
        """Test creating an instance of BaseModel with invalid keyword\
            arguments."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method of BaseModel."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the string representation of BaseModel."""
        i = self.value()
        self.assertEqual(
            str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__)
        )

    def test_todict(self):
        """Test the to_dict method of BaseModel."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """Test the id attribute of BaseModel."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute of BaseModel."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_init_no_args(self):
        """Test initializing BaseModel with no arguments."""
        i = self.value()
        self.assertIsNotNone(i.id)
        self.assertIsNotNone(i.created_at)
        self.assertIsNotNone(i.updated_at)

    def test_init_with_args(self):
        """Test initializing BaseModel with arguments."""
        id = "123"
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        i = self.value(
            id=id,
            created_at=created_at.isoformat(),
            updated_at=updated_at.isoformat(),
        )
        self.assertEqual(i.id, id)
        self.assertEqual(i.created_at, created_at)
        self.assertEqual(i.updated_at, updated_at)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        i = self.value()
        expected_str = "[{}] ({}) {}".format(self.name, i.id, i.__dict__)
        self.assertEqual(str(i), expected_str)

    def test_save_updates_updated_at(self):
        """Test that the save method updates the updated_at attribute."""
        i = self.value()
        old_updated_at = i.updated_at
        i.save()
        self.assertNotEqual(i.updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """Test that the to_dict method returns a dictionary."""
        i = self.value()
        d = i.to_dict()
        self.assertIsInstance(d, dict)

    def test_to_dict_contains_attributes(self):
        """Test that the to_dict method contains the object's attributes."""
        i = self.value()
        d = i.to_dict()
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)

    def test_delete(self):
        """Test the delete method of BaseModel."""
        i = self.value()
        i.save()
        i.delete()
        self.assertNotIn(i, storage.all().values())
