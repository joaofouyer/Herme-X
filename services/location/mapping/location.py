from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from mapping.zone import Zone
from mapping.coordinates import Coordinates

Base = declarative_base()


class Location(Base):
    __tablename__ = 'location'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    external_id = Column('external_id', Integer, nullable=True, unique=True)

    street = Column('street', String, nullable=False)
    street_number = Column('street_number', Integer, nullable=False)
    info = Column('info', String, nullable=False)
    neighborhood = Column('neighborhood', String, nullable=False)
    city = Column('city', String, nullable=False)
    state = Column('state', String, nullable=False)
    country = Column('country', String, nullable=False)
    zip_code = Column('zip_code', String, nullable=False)

    coordinates = Column(Integer, ForeignKey(Coordinates.id), nullable=False)
    zone = Column(Integer, ForeignKey(Zone.id), nullable=False)
