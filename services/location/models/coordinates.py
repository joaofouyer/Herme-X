from math import radians
from pony.orm import Database, Required

db = Database()


class Coordinates(db.Entity):
    latitude = Required(float)
    longitude = Required(float)

    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = float(latitude) if isinstance(latitude, str) else latitude
        self.longitude = float(longitude) if isinstance(longitude, str) else longitude

    def json(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def handler(self, dictionary):
        try:
            self.latitude = dictionary.get("lat", 0.0)
            if 'lon' in dictionary:
                self.longitude = dictionary['lon']
            elif 'lng' in dictionary:
                self.longitude = dictionary['lng']
            elif 'longitude' in dictionary:
                self.longitude = dictionary['longitude']
            else:
                self.longitude = 0.0

        except Exception as e:
            print("Geocoding handler exception {} {}".format(type(e), e))
            return None

    def to_radians(self):
        return radians(self.latitude), radians(self.longitude)
