import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Enum


Base = declarative_base()


class ShapeEnum(enum.Enum):
    other = 0
    boundaries = 1
    route_path = 2


class Shape(Base):
    __tablename__ = 'shape'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    external_id = Column('external_id', Integer, nullable=True, unique=True)
    shape = Column(Enum(ShapeEnum), default=0)
