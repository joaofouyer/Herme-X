import falcon
from math import cos, sin, asin, sqrt
import json
from coordinates import Coordinates
from travel_time import TravelTime


class Distance:
    def __init__(self):
        self.origin = Coordinates(latitude=0.0, longitude=0.0)
        self.destination = Coordinates(latitude=0.0, longitude=0.0)
        self.mode = "haversine"
        self.haversine_distance = 0
        self.euclidean_distance = 0
        self.driving_distance = 0

    def haversine(self):
        """
        :return: the haversine distance between two points, in meters.
        """
        try:
            ori_lat, ori_lng = self.origin.to_radians()
            des_lat, des_lng = self.destination.to_radians()

            delta_longitude = des_lng - ori_lng
            delta_latitude = des_lat - ori_lat

            a = sin(delta_latitude / 2) ** 2 + cos(ori_lat) * cos(des_lat) * sin(delta_longitude / 2) ** 2

            distance = 2 * asin(sqrt(a)) * 6371000                                             # Earth radius, in meters
            self.haversine_distance = distance
            return distance

        except Exception as e:
            print("Error on calculating Haversine Distance:  {} {}".format(type(e), e))
            raise e

    def euclidean(self):
        try:
            deglen = 119400
            delta_lat = self.origin.latitude - self.destination.latitude
            delta_lng = (self.origin.longitude - self.destination.longitude) * cos(self.destination.latitude)
            distance = deglen * sqrt(delta_lat * delta_lat + delta_lng * delta_lng)
            self.euclidean_distance = distance
            return distance
        except Exception as e:
            print("Error on calculating Euclidean distance :  {} {}".format(type(e), e))
            raise e

    def driving(self):
        try:
            travel_time = TravelTime(origin=self.origin, destination=self.destination)
            travel_time.origin = self.origin
            travel_time.destination = self.destination
            travel_time.google()
            print(self.mode)
            self.driving_distance = travel_time.distance
            return travel_time.distance
        except Exception as e:
            print("Error on calculating driving distance :  {} {}".format(type(e), e))
            raise e

    def walking(self):
        pass

    def json(self):
        distance = {
            "haversine": self.haversine_distance,
            "euclidean": self.euclidean_distance,
            "driving": self.driving_distance
        }
        return {
            "origin": self.origin.json(),
            "destination": self.destination.json(),
            "mode": self.mode,
            "distance": distance[self.mode]
        }

    def on_get(self, request, response, origin, destination, mode="haversine"):
        try:
            response.status = falcon.HTTP_200
            self.mode = mode
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

            self.origin = Coordinates(latitude=origin[0], longitude=origin[1])
            self.destination = Coordinates(latitude=destination[0], longitude=destination[1])

            options = {"haversine":  self.haversine, "euclidean": self.euclidean, "driving": self.driving}

            options[mode]()

            response.body = json.dumps(self.json())

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e


