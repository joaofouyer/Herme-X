import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum

Base = declarative_base()


class StopType(enum.Enum):
    other = 0
    totem = 1
    roof = 2


class Sidewalk(enum.Enum):
    other = 0
    sidewalk = 1
    lane = 2


class Stop(Base):
    __tablename__ = 'stop'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    external_id = Column('external_id', Integer, nullable=True, unique=True)

    address = Column(Integer, ForeignKey('location.id'), nullable=False)
    reference = Column('reference', String, nullable=True)
    stop_type = Column(Enum(StopType), nullable=False, default=0)
    sidewalk_type = Column(Enum(Sidewalk), nullable=False, default=0)
    company_id = Column('company_id', Integer, nullable=True)
