import psycopg2
import os
from sqlalchemy import create_engine
from settings.conf import DB_NAME, DB_PASS, DB_USER, DB_PORT, DB_ADDR
from mapping import *


dir_path = os.path.dirname(os.path.realpath(__file__))

HOST = "{}:{}".format(DB_ADDR, DB_PORT)

eng = "postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}".format(
    USER=DB_USER, PASSWORD=DB_PASS, HOST=HOST, DB_NAME=DB_NAME
)

engine = create_engine(eng)


def connect():
    try:
        connection = psycopg2.connect(
            user=os.environ.get('DB_USER', 'postgres'),
            password=os.environ.get('DB_PASSWORD', 'postgres'),
            host=os.environ.get('DB_ADDR', 'db'),
            port=os.environ.get('DB_PORT', '5432'),
            database=os.environ.get('DB_NAME', 'postgres')
        )
        print("Conexação com base da dados estabelecida!")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erro ao tentar conectar com a base de dados: ", error)


def start():
    try:
        Coordinates.__table__.create(bind=engine)
        Shape.__table__.create(bind=engine)
        Geocoordinates.__table__.create(bind=engine)
        Zone.__table__.create(bind=engine)
        Location.__table__.create(bind=engine)
        Stop.__table__.create(bind=engine)

    except Exception as e:
        print("Error on starting mapping on databse:  {} {}".format(type(e), e))
        raise e

# from mapping import *
# from settings.database import *
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(obj)
# session.commit()
# session.rollback()
# session.close()
# session.query(Class)
# query = session.query(Coordinates.latlng.ST_AsText()).order_by(Coordinates.id)
# puc = Coordinates(latlng='POINT(-23.549271 -46.650220)', latitude=-23.549271, longitude=-46.650220)
# scopus = Coordinates(latlng='POINT(-23.501114 -46.750878)', latitude=-23.501114, longitude=-46.750878)
# angra = Coordinates(latlng='POINT(-23.002155 -44.339088)', latitude=-23.002155, longitude=-44.339088)
# paris = Coordinates(latlng='POINT(48.690234 2.312484)', latitude=48.690234, longitude=2.312484)
# coords = Coordinates(latlng='POINT(-23.512020 -46.666161)', latitude=-23.512020, longitude=-46.666161)
# inova = Coordinates(latlng='POINT(-23.554390 -46.661982)', latitude=-23.554390, longitude=-46.661982)
# hm = Session().query(Coordinates.latlng.ST_AsText()).order_by(Coordinates.latlng.ST_Distance(inova.latlng)) WORKS
