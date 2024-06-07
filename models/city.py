#!/usr/bin/python3
"""
This module defines the City class, which represents a city in the AirBnB\
    clone v2 application.
"""

from os import getenv
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class represents a city in the AirBnB clone v2 application.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
