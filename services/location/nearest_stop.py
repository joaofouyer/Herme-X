from mapping.coordinates import Coordinates
from mapping.stop import Stop
from models.coordinates import Coordinates as Coord
from distance import Distance
from settings.database import engine
from sqlalchemy.orm import sessionmaker


class NearestStop:
    def find(self, coordinates):
        try:
            from shapely import wkb, wkt
            from binascii import unhexlify
            Session = sessionmaker(bind=engine)
            session = Session()
            d = Distance()

            n = session.query(Stop.external_id, Stop.coordinates) \
                .order_by(Stop.coordinates.ST_Distance(coordinates.latlng)).limit(1).first()

            stop_coord = wkb.loads(unhexlify("{}".format(n.coordinates)))
            d.origin = Coord(latitude=coordinates.latitude, longitude=coordinates.longitude)
            d.destination = Coord(latitude=stop_coord.x, longitude=stop_coord.y)
            distance = d.haversine()

            session.close()
            return {
                "id": n.external_id,
                "distance": distance,
                "coordinates": {
                    "latitude": stop_coord.x,
                    "longitude": stop_coord.y
                }
            }
        except Exception as e:
            print("Exception on find nearest stop: {} {}".format(type(e), e))
            raise e

    def find_multiple(self, passengers):
        try:
            for p in passengers:
                origin = [p["origin"]["latitude"], p["origin"]["longitude"]]
                point = "POINT({} {})".format(origin[0], origin[1])
                coo = Coordinates(latitude=origin[0], longitude=origin[1], latlng=point)
                stop = self.find(coordinates=coo)
                p["pickup"] = {
                    "id": stop["id"],
                    "distance": stop["distance"],
                    "coordinates": {
                        "latitude": stop["coordinates"]["latitude"],
                        "longitude": stop["coordinates"]["longitude"]
                    }
                }
                destination = [p["destination"]["latitude"], p["destination"]["longitude"]]
                point = "POINT({} {})".format(destination[0], destination[1])
                coo = Coordinates(latitude=destination[0], longitude=destination[1], latlng=point)
                stop = self.find(coordinates=coo)

                p["dropoff"] = {
                    "id": stop["id"],
                    "distance": stop["distance"],
                    "coordinates": {
                        "latitude": stop["coordinates"]["latitude"],
                        "longitude": stop["coordinates"]["longitude"]
                    }
                }

            return passengers
        except Exception as e:
            print("Exception on find multiple stops: {} {}".format(type(e), e))
            raise e
