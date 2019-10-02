import requests
import falcon
from settings import *


class TravelTime:
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
            url = 'https://maps.googleapis.com/maps/api/directions/json?' \
                  'key={key}' \
                  '&origin={origin_lat}, {origin_lng}' \
                  '&destination={dest_lat}, {dest_lng}' \
                  '&mode=driving' \
                  '&travel_mode=pessimistic' \
                .format(key=GOOGLE_DIRECTIONS, origin_lat=origin[0], origin_lng=origin[1],
                        dest_lat=destination[0], dest_lng=destination[1])

            url += "&arrival_time={}".format(arrival) if arrival else ''
            url += "&departure_time={}".format(departure) if departure else ''
            url = url.replace(' ', '')
            resp = requests.get(url)
            response.body = resp.content

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e
