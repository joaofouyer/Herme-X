from json import dumps, loads
import falcon
from settings.conf import FOWARD_PROVIDERS, REVERSE_PROVIDERS

from geocoding import Geocoding
from travel_time import TravelTime
from distance import Distance
from sync import Sync
from nearest_stop import NearestStop
from models.coordinates import Coordinates

api = falcon.API()
api.req_options.auto_parse_form_urlencoded = True


class Main:
    def on_get(self, request, response):
        try:
            response.status = falcon.HTTP_200
            description = {
                "services": {
                    "Geocoder":{
                        "description": "",
                        "usages": {
                            "Foward": " ",
                            "Reverse": ""
                        },
                        "Forward Providers": "",
                        "Reverse Providers": ""
                    },
                    "Estimate Travel Time": {
                        "description": "",
                        "usages": {
                            "Simple": "",
                            "Departure Time": "",
                            "Arrival Time": "",
                        }
                    },
                    "Distance": {
                        "description": "",
                        "usages": {
                            "Haversine": "",
                            "Euclidian": "",
                            "Driving": "",
                            "Walking": ""
                        }
                    },
                }
            }
            response.body = dumps(description)

        except Exception as e:
            print("Exception on main: {} {}".format(type(e), e))
            raise e


class GeocoderService:
    def on_get(self, request, response, address=None, latlng=None, provider=None):
        try:
            response.status = falcon.HTTP_200
            geo = Geocoding()
            geo.address = address
            geo.latlng = latlng

            if geo.address:
                geo.provider = provider if geo.provider else FOWARD_PROVIDERS[0]
                loc = geo.foward()

            elif geo.latlng:
                geo.provider = provider if geo.provider else REVERSE_PROVIDERS[0]
                geo.coord = [float(geo.latlng.split(',')[0]), float(geo.latlng.split(',')[1])]
                loc = geo.reverse()

            else:
                raise falcon.HTTPMissingParam(
                    param_name="address", href_text="You must provide at least an address or latlng param."
                )
            response.body = dumps(loc.json())

        except Exception as e:
            print("Geocoding exception {} {}".format(type(e), e))
            raise e


class TravelTimeService:
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

            tt = TravelTime()

            origin = origin.split(',')
            destination = destination.split(',')

            tt.origin = Coordinates(latitude=origin[0], longitude=origin[1])
            tt.destination = Coordinates(latitude=destination[0], longitude=destination[1])
            tt.departure = departure
            tt.arrival = arrival

            resp = tt.google()

            response.body = dumps(resp)

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e


class DistanceService:
    def on_get(self, request, response, origin, destination, mode="haversine"):
        try:
            response.status = falcon.HTTP_200
            dist = Distance()
            dist.mode = mode
            if not origin:
                raise falcon.HTTPMissingParam(
                    param_name="origin", href_text="You must provide an origin address to measure distance."
                )
            if not destination:
                raise falcon.HTTPMissingParam(
                    param_name="destination", href_text="You must provide a destination address to measure distance."
                )

            origin = origin.split(',')
            destination = destination.split(',')

            dist.origin = Coordinates(latitude=origin[0], longitude=origin[1])
            dist.destination = Coordinates(latitude=destination[0], longitude=destination[1])

            options = {"haversine": dist.haversine, "euclidean": dist.euclidean, "driving": dist.driving}

            options[mode]()
            response.body = dumps(dist.json())

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e


class NearestStopService:
    def on_get(self, request, response):
        try:
            response.status = falcon.HTTP_200
            data = loads(request.stream.read())
            ns = NearestStop()
            response.body = dumps(ns.find(addresses=data))

        except Exception as e:
            print("Exception on nearest stop: {} {}".format(type(e), e))
            raise e


class SyncService:
    def on_post(self, request, response, mode):
        try:
            data = loads(request.stream.read())

            response.status = falcon.HTTP_200
            sync = Sync()

            error = True

            if mode == "coordinates":
                error = sync.sync_coordinates(data)
            elif mode == "shape":
                error = sync.sync_shape(data)
            elif mode == "geocoordinates":
                error = sync.sync_geocoordinates(data)
            elif mode == "location":
                error = sync.sync_location(data)
            elif mode == "stop":
                error = sync.sync_stop(data)
            elif mode == "zone":
                error = sync.sync_zone(data)
            else:
                print("Sync not supported!")

            if error:
                response.status = falcon.HTTP_500

        except Exception as e:
            print("Exception on sync: {} {}".format(type(e), e))
            raise e


app = Main()

api.add_route('/', app)

geocoding = GeocoderService()

travel_time = TravelTimeService()

distance = DistanceService()

sync = SyncService()

find_stop = NearestStopService()

api.add_route('/find-stop/', find_stop)

api.add_route('/geocoder/address={address}', geocoding)
api.add_route('/geocoder/latlng={latlng}', geocoding)
api.add_route('/geocoder/', geocoding)

api.add_route('/ett/', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/departure={departure}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/arrival={arrival}', travel_time)

api.add_route('/distance/', distance)
api.add_route('/distance/origin={origin}&destination={destination}', distance)
api.add_route('/distance/{mode}/origin={origin}&destination={destination}', distance)

api.add_route('/sync/{mode}', sync)


