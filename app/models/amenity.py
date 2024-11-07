from app.persistence import Base
import uuid
import re
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship

class Amenity(Base):
    """ User class """
    __tablename__ = 'amenities'

    _name = Column("first_name", String(50), nullable=False)
    _place_id = Column("place_id", ForeignKey('place.id'), nullable=False)
    # reviews_r = relationship("Review", back_populates="user_r", cascade="delete, delete-orphan")
    # properties_r = relationship("Place", back_populates="owner_r", cascade="delete, delete-orphan")

    def __init__(self, name):
        if name is None:
            raise ValueError("Required attributes not specified!")

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
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
