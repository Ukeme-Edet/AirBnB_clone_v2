#!/usr/bin/python3
"""
This module contains the DBStorage class, which represents the database storage engine for the AirBnB clone project.
It provides methods to interact with the database, such as querying, adding, deleting, and saving objects.
"""

from models.base_model import Base, BaseModel


class DBStorage:
    """
    Represents the database storage engine for the AirBnB clone project.

    Attributes:
        __engine (sqlalchemy.engine.base.Engine): The SQLAlchemy engine instance.
        __session (sqlalchemy.orm.session.Session): The SQLAlchemy session instance.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new DBStorage instance.
        """
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        from os import getenv

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects in the database.

        Args:
            cls (class): The class of objects to retrieve.

        If cls is not None, the dictionary contains only objects of the specified class.
        Otherwise, the dictionary contains objects of all classes.
        """
        from models import storage

        if cls:
            return {
                obj.__class__.__name__ + "." + obj.id: obj
                for obj in self.__session.query(cls).all()
            }
        else:
            return {
                obj.__class__.__name__ + "." + obj.id: obj
                for obj in storage.all_classes
                for obj in self.__session.query(obj).all()
            }

    def new(self, obj):
        """
        Adds a new object to the database session.

        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database session.

        Args:
            obj (BaseModel): The object to delete from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database session.

        This method creates all the necessary tables in the database using the
        SQLAlchemy `Base.metadata.create_all` method. It then creates a session
        factory using `sessionmaker` and binds it to the engine. Finally, it creates
        a scoped session using the session factory and assigns it to the `__session`
        attribute of the `db_storage` instance.

        Note:
        - The `expire_on_commit` parameter is set to `False` to prevent objects from
            being expired after each commit.

        Returns:
        None
        """
        from sqlalchemy.orm import scoped_session, sessionmaker

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
