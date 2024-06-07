#!/usr/bin/python3
"""
This module defines the DBStorage class, which is responsible for interacting\
    with the database.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    This class represents the database storage for the AirBnB clone project.
    It provides methods to interact with the database, such as retrieving\
        objects,
    adding new objects, saving changes, deleting objects, and reloading the \
        session.

    Attributes:
        __engine (object): The database engine.
        __session (object): The database session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.
        It creates a database engine and sets up the session.
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True,
            )
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects from the database.

        Args:
            cls (str): The class name of the objects to retrieve. If None,\
                retrieves all objects.

        Returns:
            dict: A dictionary of objects, where the key is the object's class\
                name and ID.
        """
        objects = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                objects[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for table in Base.metadata.tables.keys():
                for obj in self.__session.query(eval(table)).all():
                    objects[obj.__class__.__name__ + "." + obj.id] = obj
        return objects

    def new(self, obj):
        """
        Adds a new object to the session.

        Args:
            obj: The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits the session to save any changes made to the objects.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the session.

        Args:
            obj: The object to delete from the session. If None, does nothing.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the session and creates all tables in the database.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        self.__session.configure(bind=self.__engine)
        self.__session.expire_on_commit = False
        self.__session.expire_all()
