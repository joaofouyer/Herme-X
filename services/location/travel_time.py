import requests
import falcon
import json
from requests.utils import get_unicode_from_response
from coordinates import Coordinates
from settings import *


class TravelTime:
    """
    Both origin and destination must be in a coordinate system.
    If desired, the departure or arrival time can be passed to estimate more precisely. It should be in Unix timestamp
    The distance is given in meters.
    The duration is given in seconds.
    """
    def __init__(self, origin=None, destination=None):
        if origin:
            self.origin = origin
        else:
            self.origin = Coordinates(latitude=0.0, longitude=0.0)
        if destination:
            self.destination = destination
        else:
            self.destination = Coordinates(latitude=0.0, longitude=0.0)
        self.duration = None
        self.departure = None
        self.arrival = None
        self.distance = None

    def mapbox(self):
        try:
            pass
        except Exception as e:
            print("TravelTime by mapbox directions failed: {} {}".format(type(e), e))
            raise e

    def google(self):
        try:
            url = 'https://maps.googleapis.com/maps/api/directions/json?' \
                  'key={key}' \
                  '&origin={origin_lat}, {origin_lng}' \
                  '&destination={dest_lat}, {dest_lng}' \
                  '&mode=driving' \
                  '&travel_mode=pessimistic' \
                .format(key=GOOGLE_DIRECTIONS, origin_lat=self.origin.latitude, origin_lng=self.origin.longitude,
                        dest_lat=self.destination.latitude, dest_lng=self.destination.longitude)

            url += "&arrival_time={}".format(self.arrival) if self.arrival else ''
            url += "&departure_time={}".format(self.departure) if self.departure else ''
            url = url.replace(' ', '')
            directions = json.loads(get_unicode_from_response(requests.get(url)))
            if directions['status'] == 'INVALID_REQUEST' or directions['status'] == 'ZERO_RESULTS':
                description = directions['error_message'] if 'error_message' in directions else ''
                raise falcon.HTTPBadRequest(title="INVALID REQUEST", description=description)
            else:
                self.distance = directions["routes"][0]["legs"][0]["distance"]["value"]
                self.duration = directions["routes"][0]["legs"][0]["duration"]["value"]
                return directions
        except Exception as e:
            print("TravelTime by google directions failed: {} {}".format(type(e), e))
            raise e

    def on_get(self, request, response, origin, destination, departure=None, arrival=None):
        try:
            response.status = falcon.HTTP_200
            if not origin:
                raise falcon.HTTPMissingParam(
                    param_name="origin", href_text="You must provide an origin address to estimate travel time."
                )
            if not destination:
                raise falcon.HTTPMissingParam(
                    param_name="destination", href_text="You must provide destination address to estimate travel time."
                )

            origin = origin.split(',')
            destination = destination.split(',')

            self.origin = Coordinates(latitude=origin[0], longitude=origin[1])
            self.destination = Coordinates(latitude=destination[0], longitude=destination[1])
            self.departure = departure
            self.arrival = arrival

            resp = self.google()

            response.body = json.dumps(resp)

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e
