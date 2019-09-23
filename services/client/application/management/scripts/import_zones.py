import json
from application.models import Zone, Geometry, Coordinates, Geocoordinates
from tqdm import tqdm


def import_movement_zones():
    try:
        file = open("/code/datasets/movement/zones.json", mode="r")
        zones = json.load(file)['features']
        for zone in tqdm(zones):
            if not Zone.objects.filter(movement_id=zone['properties']['MOVEMENT_ID']).count():
                geometry = Geometry(
                    type=1
                )
                geometry.save()
                for coordinate in tqdm(zone['geometry']['coordinates'][0]):
                    if isinstance(coordinate[0], list):
                        for coord in coordinate:
                            create_geo_coordinates(coordinates=coord, geometry=geometry)
                    else:
                        create_geo_coordinates(coordinates=coordinate, geometry=geometry)
                p = zone['properties']
                z = Zone(
                    type=1, name=p['NomeZona'], number=p['NumeroZona'], district_name=p['NomeDistri'],
                    district_number=p['NumDistrit'], city_name=p['NomeMunici'], city_number=p['NumeroMuni'],
                    movement_id=p['MOVEMENT_ID'], geometry=geometry
                )
                z.save()

        return False
    except Exception as e:
        print("Exceção em import_zones: ", e)
        return True


def create_geo_coordinates(coordinates, geometry):
    try:
        coordinates_query = Coordinates.objects.filter(latitude=coordinates[1], longitude=coordinates[0])
        if coordinates_query.count():
            c = coordinates_query.first()
        else:
            c = Coordinates(
                latitude=coordinates[1],
                longitude=coordinates[0],
            )
            c.save()

        geo_coords = Geocoordinates(coordinates=c, geometry=geometry)
        geo_coords.save()
        return geo_coords

    except Exception as e:
        print("Exception on create_geo_coordinates:", e)
        return None
