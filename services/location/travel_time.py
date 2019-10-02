import requests
import falcon

from coordinates import Coordinates
from settings import *


class TravelTime:
    def __init__(self):
        self.origin = Coordinates(latitude=0.0, longitude=0.0)
        self.destination = Coordinates(latitude=0.0, longitude=0.0)
        self.duration = None
        self.departure = None
        self.arrival = None

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
            return requests.get(url)
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

            response.body = resp.content

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e
