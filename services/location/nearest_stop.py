from mapping.coordinates import Coordinates
from mapping.stop import Stop
from models.coordinates import Coordinates as Coord
from distance import Distance
from settings.database import engine
from sqlalchemy.orm import sessionmaker


class NearestStop:
    def find(self, addresses):
        from shapely import wkb, wkt
        from binascii import unhexlify
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            d = Distance()
            stops = []
            for a in addresses:
                if isinstance(a, dict):
                    lat = a['latitude']
                    lng = a['longitude']
                else:
                    lat = a[0]
                    lng = a[1]
                    a = {
                        "latitude": lat,
                        "longitude": lng
                    }
                point = "POINT({} {})".format(lat, lng)
                coo = Coordinates(latitude=lat, longitude=lng, latlng=point)

                n = session.query(Stop.external_id, Stop.coordinates) \
                    .order_by(Stop.coordinates.ST_Distance(coo.latlng)).limit(1).first()

                stop_coord = wkb.loads(unhexlify("{}".format(n.coordinates)))
                d.origin = Coord(latitude=lat, longitude=lng)
                d.destination = Coord(latitude=stop_coord.x, longitude=stop_coord.y)
                distance = d.haversine()
                a['nearest_stop'] = {
                    "id": n.external_id,
                    "distance": distance
                }
                stops.append(a)
            session.close()
            return stops
        except Exception as e:
            print("Exception on find nearest stop: {} {}".format(type(e), e))
            raise e
