#!/usr/bin/python3

""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from models import storage
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return the list of City instances with
            state_id equals to the current State.id
            """
            value_cy = storage.all(City).values()
            list_cy = []
            for city in value_cy:
                if city.state_id == self.id:
                    list_cy.append(city)
            return list_cy
