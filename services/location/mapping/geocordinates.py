from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey

from mapping.shape import Shape
from mapping.coordinates import Coordinates

Base = declarative_base()


class Geocoordinates(Base):
    __tablename__ = 'geocoordinates'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    external_id = Column('external_id', Integer, nullable=True, unique=True)

    coordinates_id = Column(Integer, ForeignKey(Coordinates.id))
    geometry_id = Column(Integer, ForeignKey(Shape.id))
