import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User


class TestDBStorage(unittest.TestCase):
    """
    This class contains unit tests for the DBStorage class.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of the DBStorage class.
        """
        self.storage = DBStorage()

    def tearDown(self):
        """
        Clean up the test environment by deleting the instance of the DBStorage class.
        """
        pass

    def test_all(self):
        """
        Test the all method in the DBStorage class.

        This test case checks if the all method returns a dictionary of objects.
        """
        # Create some test objects
        base_model = BaseModel()
        user = User()

        # Add the test objects to the session
        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.save()

        # Retrieve all objects from the session
        objects = self.storage.all()

        # Check if the objects are in the dictionary
        self.assertIn(
            base_model.__class__.__name__ + "." + base_model.id, objects
        )
        self.assertIn(user.__class__.__name__ + "." + user.id, objects)

    def test_new(self):
        """
        Test the new method in the DBStorage class.

        This test case checks if the new method adds a new object to the session.
        """
        # Create a test object
        base_model = BaseModel()

        # Add the test object to the session
        self.storage.new(base_model)
        self.storage.save()

        # Retrieve all objects from the session
        objects = self.storage.all()

        # Check if the test object is in the dictionary
        self.assertIn(
            base_model.__class__.__name__ + "." + base_model.id, objects
        )

    def test_delete(self):
        """
        Test the delete method in the DBStorage class.

        This test case checks if the delete method deletes an object from the session.
        """
        # Create a test object
        base_model = BaseModel()

        # Add the test object to the session
        self.storage.new(base_model)
        self.storage.save()

        # Delete the test object from the session
        self.storage.delete(base_model)
        self.storage.save()

        # Retrieve all objects from the session
        objects = self.storage.all()

        # Check if the test object is not in the dictionary
        self.assertNotIn(
            base_model.__class__.__name__ + "." + base_model.id, objects
        )
