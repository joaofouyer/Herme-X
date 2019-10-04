from math import radians
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
from geoalchemy2 import Geography


Base = declarative_base()


class Coordinates(Base):
    __tablename__ = 'coordinates'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)

    latitude = Column('latitude', Float, nullable=False)
    longitude = Column('longitude', Float, nullable=False)

    latlng = Column(
        'latlng',
        Geography(geometry_type='POINT', dimension=2, spatial_index=True),
        nullable=False,
        unique=True
    )

    external_id = Column('external_id', Integer, nullable=True, unique=True)

    def to_radians(self):
        return radians(self.latitude), radians(self.longitude)
