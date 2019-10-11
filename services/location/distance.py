from math import cos, sin, asin, sqrt
from models.coordinates import Coordinates
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

    def sort(self, places):
        try:
            print(places)
        except Exception as e:
            print("Error on sorting distances:  {} {}".format(type(e), e))
            raise e

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
