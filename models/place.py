#!/usr/bin/python3

""" Place Module for HBNB project """

from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False
        )

    else:
        @property
        def amenities(self):
            """Getter attribute for amenities when using FileStorage"""
            from models import storage
            from models.amenity import Amenity

            amenity_instances = []
            for amenity_id in self.amenity_ids:
                key = "Amenity." + amenity_id
                amenity_instance = storage.all(Amenity).get(key)
                if amenity_instance:
                    amenity_instances.append(amenity_instance)
            return amenity_instances

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute for amenities when using FileStorage"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
