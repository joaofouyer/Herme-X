def get_address_boundaries(coordinates, degrees=0.005):
    try:
        lat, lng = coordinates[0], coordinates[1]
        area_lat = float(lat) - degrees, float(lat) + degrees
        area_lng = float(lng) - degrees, float(lng) + degrees

        return area_lat, area_lng
    except Exception as e:
        print("Error on get_address_boundaries :  {} {}".format(type(e), e))
        raise e