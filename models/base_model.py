#!/usr/bin/python3
"""
This module contains the BaseModel class, which serves as the base class for\
    all models in the application.

Attributes:
    id (str): The unique identifier for the model instance.
    created_at (datetime): The datetime when the model instance was created.
    updated_at (datetime): The datetime when the model instance was last\
        updated.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of the\
        BaseModel class.
    __str__(self): Returns a string representation of the BaseModel instance.
    save(self): Saves the BaseModel instance to the database.
    to_dict(self): Converts the BaseModel instance to a dictionary.
    delete(self): Deletes the BaseModel instance from the database.
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    Represents the base model for all other models in the application.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The timestamp indicating when the instance was\
            created.
        updated_at (datetime): The timestamp indicating when the instance was\
            last updated.
    """

    from datetime import timezone

    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(
        DateTime, default=datetime.now(timezone.utc), nullable=False
    )
    updated_at = Column(
        DateTime, default=datetime.now(timezone.utc), nullable=False
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty, the instance attributes are set based on the\
            key-value pairs
        in kwargs. Otherwise, the instance attributes are set with default\
            values.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                kwargs["created_at"] = datetime.now()
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                kwargs["updated_at"] = datetime.now()
            if "__class__" in kwargs:
                del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Saves the BaseModel instance to the database.
        """
        self.updated_at = datetime.now()
        from models import storage

        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """
        Deletes the BaseModel instance from the database.
        """
        from models import storage

        storage.delete(self)
        storage.save()
