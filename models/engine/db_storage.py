#!/usr/bin/python3
"""
This module defines the DBStorage class, which is responsible for interacting with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.
        It creates a database engine and sets up the session.
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects from the database.

        Args:
            cls (str): The class name of the objects to retrieve. If None, retrieves all objects.

        Returns:
            dict: A dictionary of objects, where the key is the object's class name concatenated with its ID.
        """
        new_dict = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = obj.__class__.__name__ + "." + obj.id
                new_dict[key] = obj
        else:
            for table in Base.metadata.tables.keys():
                for obj in self.__session.query(eval(table)).all():
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        Adds a new object to the current session.

        Args:
            obj: The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits the current session, saving any changes made to the objects.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current session.

        Args:
            obj: The object to delete from the session. If None, does nothing.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database tables and sets up a new session.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """
        Closes the current session.
        """
        self.__session.close()
