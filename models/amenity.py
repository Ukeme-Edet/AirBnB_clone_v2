#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a specific feature or service provided by a property.
    """

    name = ""
