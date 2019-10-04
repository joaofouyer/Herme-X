from math import asin, sin, sqrt, cos


def haversine(origin, destination):
    try:
        ori_lat, ori_lng = origin.to_radians()
        des_lat, des_lng = destination.to_radians()

        delta_longitude = des_lng - ori_lng

        delta_latitude = des_lat - ori_lat

        a = sin(delta_latitude / 2) ** 2 + cos(ori_lat) * cos(des_lat) * sin(delta_longitude / 2) ** 2

        distance = 2 * asin(sqrt(a)) * 6371000  # Earth radius, in meters
        return distance

    except Exception as e:
        print("Error on calculating Haversine Distance:  {} {}".format(type(e), e))
        raise e


def get_address_boundaries(coordinates, degrees=0.005):
    try:
        lat, lng = coordinates[0], coordinates[1]
        area_lat = float(lat) - degrees, float(lat) + degrees
        area_lng = float(lng) - degrees, float(lng) + degrees

        return area_lat, area_lng
    except Exception as e:
        print("Error on get_address_boundaries :  {} {}".format(type(e), e))
        raise e

