""" User model """

from app.persistence import Base
import uuid
import re
from datetime import datetime
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship

bcrypt = Bcrypt()

class User(Base):
    """ User class """
    __tablename__ = 'users'

    # Remember: if you have getters & setters for any of the attributes
    # you can't use the same name for the attributes themselves

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())
    _first_name = Column("first_name", String(50), nullable=False)
    _last_name = Column("last_name", String(50), nullable=False)
    _email = Column("email", String(120), nullable=False, unique=True)
    _password = Column("password", String(128), nullable=False)
    _is_admin = Column("is_admin", Boolean, default=False)
    # reviews_r = relationship("Review", back_populates="user_r", cascade="delete, delete-orphan")
    # properties_r = relationship("Place", back_populates="owner_r", cascade="delete, delete-orphan")

    def __init__(self, first_name, last_name, email, password=None, is_admin = False):
        # NOTE: Attributes that don't already exist will be
        # created when called in the constructor

        if first_name is None or last_name is None or email is None:
            raise ValueError("Required attributes not specified!")

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # List to store user-owned places
        self.reviews = [] # List to store user-written reviews

        # The method will call the setter
        # self.hash_password(password)
