import json

from application.management.scripts import sptrans_to_json
from application.models import Zone, Geometry, Coordinates, Geocoordinates, Stop, Location
from tqdm import tqdm


def import_stops():
    try:
        file = open("/code/datasets/sptrans/stops.json", mode="r")
        create_stops(json.load(file))

        return False
    except FileNotFoundError:
        stops = sptrans_to_json()
        create_stops(json.loads(stops))
    except Exception as e:
        print("Exceção {} em import_stops: {}".format(type(e), e.message))
        return True


def create_stops(stops):
    try:
        for stop in tqdm(stops):
            coordinates = Coordinates(
                latitude=stop['address']['coordinates']['latitude'],
                longitude=stop['address']['coordinates']['longitude']
            )
            coordinates.save()
            location = Location(
                coordinates=coordinates,

            )

        return False
    except Exception as e:
        print("Exceção {} em import_stops: {}".format(type(e), e.message))
        return True