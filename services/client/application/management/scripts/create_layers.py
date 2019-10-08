import json
from application.models import Passenger
from tqdm import tqdm

# from application.management.scripts.create_layers import do


def do():
    try:
        passengers = Passenger.objects.all()
        dicts = {
            "type": "FeatureCollection",
            "features": []
        }
        for p in tqdm(passengers):
            print(p.home_address)
            # print(p.destination.coordinates)
            dicts['features'].append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [p.home_address.coordinates.longitude, p.home_address.coordinates.latitude]
                    },
                    "properties": {
                        "type": "origin",
                        "passenger": p.id,
                        "address": p.home_address.street
                    }
                }
            )

            dicts['features'].append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [p.destination.coordinates.longitude, p.destination.coordinates.latitude]
                    },
                    "properties": {
                        "type": "destination",
                        "passenger": p.id,
                        "address": p.destination.street
                    }
                }
            )

        dicts = json.dumps(dicts, ensure_ascii=False).encode('utf8')
        print(type(dicts))
        with open("/code/application/static/layers/passengers.json", 'w') as fp:
            fp.write(dicts.decode())
        return False
    except Exception as e:
        print("Exceção em create_stop_layer: ", e)
        return True
