#!/usr/bin/python3
"""
This module defines the City class, which represents a city in the AirBnB\
    clone v2 application.
"""

from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    City class represents a city in the AirBnB clone v2 application.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty, the instance attributes are set based on the\
            key-value pairs
        in kwargs. Otherwise, the instance attributes are set with default\
            values.
        """
        super().__init__(*args, **kwargs)
