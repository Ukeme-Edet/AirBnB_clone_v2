#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """
    This class represents a file storage system for storing and retrieving\
        objects.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary containing all objects currently\
            stored in the FileStorage.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects in the storage.

        If a class is specified, it returns a dictionary of objects of that\
            class.
        If no class is specified, it returns a dictionary of all objects in\
            the storage.

        Args:
            cls (class, optional): The class to filter the objects by.\
                Defaults to None.

        Returns:
            dict: A dictionary of objects in the storage.
        """
        if cls:
            return {
                key: val
                for key, val in self.__objects.items()
                if val.__class__ == cls
            }
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.

        Returns:
            None
        """
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """
        Saves the objects in the FileStorage to a JSON file.

        This method iterates over the objects stored in the FileStorage,
        converts them to dictionaries using the `to_dict` method, and
        saves them to a JSON file.

        Returns:
            None
        """
        temp = {}
        for key, val in self.all().items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(temp, f)

    def reload(self):
        """
        Reloads objects from JSON file.

        This method reads the JSON file specified by `FileStorage\
            __file_path` and
        reloads the objects stored in it. It imports the necessary model\
            classes
        and creates instances of those classes using the data from the JSON\
            file.

        Returns:
            None
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside.

        Args:
            obj: The object to be deleted.

        Returns:
            None
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
            self.save()
