#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    from datetime import timezone

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(
        DateTime, nullable=False, default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now(timezone.utc)
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the object.

        The string representation includes the class name, the object's id,
        and the object's attributes.

        Returns:
            str: The string representation of the object.
        """
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime and\
            saves the instance to the storage.
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the object attributes to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object attributes.
        """
        ret = self.__dict__.copy()
        ret["__class__"] = str(type(self)).split(".")[-1].split("'")[0]
        ret["updated_at"] = self.updated_at.isoformat()
        ret["created_at"] = self.created_at.isoformat()
        if "_sa_instance_state" in ret:
            del ret["_sa_instance_state"]
        return ret

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        from models import storage

        storage.delete(self)
