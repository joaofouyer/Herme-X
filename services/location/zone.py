class Zone:
    def __init__(self, type, name, number, district_name, district_number, city_name, city_number, movement_id,
                 geometry=None):
        self.type = type
        self.name = name
        self.number = number
        self.district_name = district_name
        self.district_number = district_number
        self.city_name = city_name
        self.city_number = city_number
        self.movement_id = movement_id
        self.geometry = geometry

    @staticmethod
    def json():
        return {}

    @staticmethod
    def handler(dictionary):
        return None
