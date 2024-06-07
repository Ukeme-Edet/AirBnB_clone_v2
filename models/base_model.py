#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class for all models in the application.
"""

import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:
    """The base class for all models in the application."""

    id = Column(String(60), primary_key=True, nullable=False)
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
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                elif key != "__class__":
                    setattr(self, key, value)
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Saves the BaseModel instance to the storage.

        This method updates the `updated_at` attribute and calls the `new` and `save` methods of the storage.
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            A dictionary representation of the BaseModel instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def delete(self):
        """
        Deletes the BaseModel instance from the storage.

        This method calls the `delete` and `save` methods of the storage.
        """
        from models import storage

        storage.delete(self)
        storage.save()
