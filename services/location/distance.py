import requests
import falcon

from coordinates import Coordinates
from settings import *
from math import radians, cos, sin, asin, sqrt

# 4468.818397728552 m
# 4468.489208841052 m
class Distance:
    def __init__(self):
        self.origin = Coordinates(latitude=0.0, longitude=0.0)
        self.destination = Coordinates(latitude=0.0, longitude=0.0)
        self.mode = "haversine"
        self.haversine_distance = 0
        self.euclidian_distance = 0
        self.real_distance = 0

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

            return distance

        except Exception as e:
            print("Error on Distance Haversine:  {} {}".format(type(e), e))
            raise e

    def euclidean(self):
        try:
            deglen = 119400
            delta_lat = self.origin.latitude - self.destination.latitude
            delta_lng = (self.origin.longitude - self.destination.longitude) * cos(self.destination.latitude)
            return deglen * sqrt(delta_lat * delta_lat + delta_lng * delta_lng)
            # return sqrt(delta_latitude ** 2 + delta_longitude ** 2)
        except Exception as e:
            print("euclidian: ", e)
            return None

    def driving(self):
        pass

    def walking(self):
        pass

    def on_get(self, request, response, origin, destination, mode="haversine"):
        try:
            response.status = falcon.HTTP_200
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
            distance = self.euclidean()
            print(distance)

            # response.body = resp.content

        except Exception as e:
            print("Estimate Travel Time exception {} {}".format(type(e), e))
            raise e
