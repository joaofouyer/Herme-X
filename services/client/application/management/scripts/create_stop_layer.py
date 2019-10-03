import json
from application.models import Stop
from tqdm import tqdm

# from application.management.scripts.create_stop_layer import do
def do():
    try:
        stops = Stop.objects.all()
        dicts = {
            "type": "FeatureCollection",
            "features": []
        }
        for s in tqdm(stops):
            dicts['features'].append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [s.address.coordinates.longitude, s.address.coordinates.latitude]
                    },
                    "properties": {
                        "name": s.id,
                        "address": s.address.street
                    }
                }
            )

        dicts = json.dumps(dicts, ensure_ascii=False).encode('utf8')
        print(type(dicts))
        with open("/code/application/static/layers/layers.json", 'w') as fp:
            fp.write(dicts.decode())
        return False
    except Exception as e:
        print("Exceção em create_stop_layer: ", e)
        return True
