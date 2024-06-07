#!/usr/bin/python3
"""
This module contains the Review class, which represents a review for a place\
    in the AirBnB clone project.
"""

from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Review class represents a review for a place in the AirBnB clone project.

    Attributes:
        text (str): The text content of the review.
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
