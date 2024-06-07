#!/usr/bin/python3
"""
This module defines the Place class, which represents a place in the AirBnB\
    clone application.
"""
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    Place class represents a place in the AirBnB clone application.

    Attributes:
        __tablename__ (str): The name of the database table for places.
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete")
    else:

        @property
        def reviews(self):
            """
            Getter method for the reviews attribute.

            Returns:
                A list of Review instances with place_id equal to the current\
                    Place instance's id.
            """
            from models import storage
            from models.review import Review

            reviews = storage.all(Review)
            return [
                review
                for review in reviews.values()
                if review.place_id == self.id
            ]
