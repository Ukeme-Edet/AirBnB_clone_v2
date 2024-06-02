#!/usr/bin/python3
from models.base_model import Base


class DBStorage:
    """
    This class represents the database storage engine for the AirBnB clone\
        project.
    It provides methods to interact with the database, such as querying,\
        adding, deleting, and saving objects.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.
        It creates a database engine and sets up a session to interact with\
            the database.
        """
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from os import getenv

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects from the database.

        Args:
            cls (class, optional): The class of objects to retrieve. If None,\
                retrieves all objects of all classes.

        Returns:
            dict: A dictionary of objects, where the keys are in the format\
                "<class_name>.<object_id>".
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        objs = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                objs[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for cls in classes:
                for obj in self.__session.query(cls):
                    objs[obj.__class__.__name__ + "." + obj.id] = obj
        return objs

    def new(self, obj):
        """
        Adds a new object to the database session.

        Args:
            obj: The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits the changes made in the current session to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database session.

        Args:
            obj (optional): The object to delete from the session. If None,\
                does nothing.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database session and creates the necessary tables if they\
            don't exist.
        """
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import BaseModel

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
