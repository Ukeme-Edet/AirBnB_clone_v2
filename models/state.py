#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = []
    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Get a list of all cities in this state"""
            from models import storage
            from models.city import City

            cities = storage.all(City)
            return [
                city for city in cities.values() if city.state_id == self.id
            ]

    else:
        from sqlalchemy.orm import relationship

        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
        )
