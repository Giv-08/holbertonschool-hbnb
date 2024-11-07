import uuid
import re
from app.persistence import Base
from datetime import datetime
from sqlalchemy import Column, String, Integer
from .base import BaseModel
from sqlalchemy.orm import relationship

class Amenity(Base):
    """ Amenity class """
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)

    places_r = relationship("Place", back_populates='amenities_r')

    def __init__(self, name):
        if name is None:
            raise ValueError("Required attributes not specified!")

        self.name = name

    # --- Getters and Setters ---
    @property
    def name(self):
        """ Returns value of property name """
        return self._name

    @name.setter
    def name(self, value):
        """Setter for prop name"""
        # ensure that the value is up to 50 characters after removing excess white-space
        is_valid_name = 0 < len(value.strip()) <= 50
        if is_valid_name:
            self._name = value.strip()
        else:
            raise ValueError("Invalid name length!")

    # --- Methods ---
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
