#!/usr/bin/python3
""" Class State"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

# Accessing storage_t from environment variables
storage_t = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """Class of state """
    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if storage_t != "db":
        @property
        def cities(self):
            """Gets list of city instances"""
            city_list = []
            all_cities = models.storage.all(models.city.City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
