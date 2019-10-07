from sqlalchemy.orm import sessionmaker
from settings.database import engine
import time


class Sync:
    @staticmethod
    def sync_coordinates(coordinates):
        from mapping.coordinates import Coordinates

        Session = sessionmaker(bind=engine)
        session = Session()
        session.close()
        session = Session()

        try:
            print("Syncing Coordinates: ", len(coordinates))
            synced = 0
            for c in coordinates:
                point = "POINT({} {})".format(c['latitude'], c['longitude'])
                if not session.query(Coordinates).filter(Coordinates.latlng.ST_AsText() == point).count():
                    coord = Coordinates(latlng=point, latitude=c['latitude'], longitude=c['longitude'],
                                        external_id=c['id'])
                    session.add(coord)
                    synced = synced + 1
                    session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_coordinates: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def sync_geocoordinates(geocoordinates):
        try:
            from mapping import Coordinates as Coord
            from mapping import Shape
            from mapping import Geocoordinates as Geo

            Session = sessionmaker(bind=engine)
            session = Session()
            session.close()
            session = Session()
            print("Syncing Geocoordinates: ", len(geocoordinates))
            synced = 0
            for g in geocoordinates:

                if not session.query(Geo.external_id).filter(Geo.external_id == g['id']).count():

                    point = "POINT({} {})".format(g['coordinates']['latitude'], g['coordinates']['longitude'])

                    coord_id = session.query(Coord.id).filter(Coord.latlng.ST_AsText() == point)

                    shape_id = session.query(Shape.id).filter(Shape.external_id == g['geometry']['id'])

                    geo = Geo(external_id=g['id'], coordinates_id=coord_id, geometry_id=shape_id)

                    session.add(geo)

                    synced = synced + 1
            session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_geocoordinates: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def sync_location(locations):
        from mapping.location import Location
        from mapping.coordinates import Coordinates
        from mapping.zone import Zone
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            session.close()
            session = Session()
            zone = session.query(Zone.id).filter(Zone.id == 1)
            print("Syncing Locations: ", len(locations))
            synced = 0
            for l in locations:
                # if not session.query(Location).filter(Location.external_id == l['id']).count():
                point = "POINT({} {})".format(l['coordinates']['latitude'], l['coordinates']['longitude'])
                # zone = session.query(Zone.id).filter(Zone.external_id == l['zone']['id'])
                coordinates = session.query(Coordinates.id).filter(Coordinates.latlng == point)
                location = Location(
                    external_id=l['id'],
                    street=l['street'],
                    street_number=l['street_number'],
                    info=l['info'],
                    neighborhood=l['neighborhood'],
                    city=l['city'],
                    state=l['state'],
                    country=l['country'],
                    zip_code=l['zip_code'],
                    coordinates=coordinates,
                    zone=zone
                )
                session.add(location)
                synced = synced + 1
            session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_location: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def sync_shape(shapes):
        from mapping.shape import Shape, ShapeEnum

        Session = sessionmaker(bind=engine)
        session = Session()
        session.close()
        session = Session()

        try:
            print("Syncing Shapes: ", len(shapes))
            synced = 0
            for s in shapes:
                if not session.query(Shape).filter(Shape.external_id == s['id']).count():
                    type = ShapeEnum(s['type'])
                    shape = Shape(external_id=s['id'], shape=type)
                    session.add(shape)
                    synced = synced + 1
            session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_shape: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def sync_stop(stops):
        from mapping.stop import Stop, Sidewalk, StopType
        from mapping.location import Location

        Session = sessionmaker(bind=engine)
        session = Session()
        session.close()
        session = Session()

        try:
            print("Syncing Stops: ", len(stops))
            synced = 0
            for s in stops:
                # if not session.query(Stop).filter(Stop.external_id == s['id']).count():
                location_id = session.query(Location.id).filter(Location.external_id == s['address']['id'])
                if location_id.count():
                    location_id = location_id.one()
                    sidewalk = Sidewalk(value=s['sidewalk'])
                    stype = StopType(value=s['type'])
                    stop = Stop(
                        external_id=s['id'],
                        address=location_id,
                        reference=s['reference'],
                        stop_type=stype,
                        sidewalk_type=sidewalk,
                        company_id=s['company_id']
                    )
                    session.add(stop)
                    synced = synced + 1
                else:
                    print("Not found: ", s['address']['id'])
            session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_stop: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def sync_zone(zones):
        from mapping.zone import Zone, ZoneType
        from mapping.shape import Shape, ShapeEnum

        Session = sessionmaker(bind=engine)
        session = Session()
        session.close()
        session = Session()

        try:
            print("Syncing Zones: ", len(zones))
            synced = 0
            for z in zones:
                if not session.query(Zone.id).filter(Zone.external_id == z['id']).count():
                    shape_id = session.query(Shape.id).filter(Shape.external_id == z['geometry']['id'])
                    ztype = ZoneType(value=z['type'])
                    zone = Zone(
                        external_id=z['id'],
                        zone_type=ztype,
                        name=z['name'],
                        number=z['number'],
                        district_name=z['district_name'],
                        district_number=z['district_number'],
                        city_name=z['city_name'],
                        city_number=z['city_number'],
                        movement_id=z['movement_id'],
                        geometry=shape_id,
                    )
                    session.add(zone)
                    synced = synced + 1
            session.commit()
            session.close()
            print("Finished: ", synced)
            return None
        except Exception as e:
            print("Exception on sync_zone: {} {}".format(type(e), e))
            raise e
