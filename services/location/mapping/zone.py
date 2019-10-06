import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from mapping.shape import Shape
from mapping.coordinates import Coordinates


Base = declarative_base()


class ZoneType(enum.Enum):
    other = 0
    uber_movement = 1


class Zone(Base):
    __tablename__ = 'zone'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    external_id = Column('external_id', Integer, nullable=True, unique=True)
    zone_type = Column(Enum(ZoneType), nullable=False)

    name = Column('name', String, nullable=False)
    number = Column('number', Integer, nullable=True)
    district_name = Column('district_name', String, nullable=True)
    district_number = Column('district_number', Integer, nullable=True)
    city_name = Column('city_name', String, nullable=True)
    city_number = Column('city_number', Integer, nullable=True)
    movement_id = Column('movement_id', String, nullable=True)
    geometry = Column(Integer, ForeignKey(Shape.id), nullable=False)

    min_lat = Column(Integer, ForeignKey(Coordinates.id), nullable=True)
    min_lng = Column(Integer, ForeignKey(Coordinates.id), nullable=True)
    max_lat = Column(Integer, ForeignKey(Coordinates.id), nullable=True)
    max_lng = Column(Integer, ForeignKey(Coordinates.id), nullable=True)
