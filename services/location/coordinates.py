class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude) if isinstance(latitude, str) else latitude
        self.longitude = float(longitude) if isinstance(longitude, str) else longitude

    def json(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    @staticmethod
    def handler(dictionary):
        try:
            latitude = dictionary.get("lat", 0.0)
            if 'lon' in dictionary:
                longitude = dictionary['lon']
            elif 'lng' in dictionary:
                longitude = dictionary['lng']
            elif 'longitude' in dictionary:
                longitude = dictionary['longitude']
            else:
                longitude = 0.0
            return Coordinates(latitude=latitude, longitude=longitude)
        except Exception as e:
            print("Exception on Coordinates handler: ", e)
            return None
