#!/usr/bin/python3
"""
This module defines the State class.

State class represents a state in the AirBnB clone project.
It inherits from the BaseModel class and is mapped to the "states" table in\
    the database.
"""

from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state in the application.

    Attributes:
        __tablename__ (str): The name of the database table for states.
        name (str): The name of the state.
        cities (list): A list of cities associated with the state.

    Methods:
        __init__(self, *args, **kwargs): Initializes a new instance of the\
            State class.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """
            Retrieves a list of cities associated with the state.

            Returns:
                list: A list of City instances associated with the state.
            """
            from models import storage
            from models.city import City

            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
