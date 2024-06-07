#!/usr/bin/python3
"""
This module defines the Amenity class and the place_amenity table.

Amenity class represents an amenity that can be associated with a place.
The place_amenity table is a many-to-many relationship table between places\
    and amenities.
"""
from sqlalchemy import Column, ForeignKey, String, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an amenity in the AirBnB clone application.

    Attributes:
        name (str): The name of the amenity.
        place_amenity (relationship): The relationship between the amenity and\
            the place.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = relationship("Place", secondary="place_amenity")
