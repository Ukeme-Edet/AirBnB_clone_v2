#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    User class represents a user in the system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty, the instance attributes are set based on the\
            key-value pairs
        in kwargs. Otherwise, the instance attributes are set with defaul\
              values.
        """
        super().__init__(*args, **kwargs)
