from math import asin, sin, sqrt, cos
import json


def create_cluster_layer(clusters):
    try:
        dicts = {
            "type": "FeatureCollection",
            "features": []
        }
        label = 0
        for c in clusters:
            for item in c:
                dicts['features'].append(
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [item[1], item[0]]
                        },
                        "properties": {
                            "group": str(label)
                        }
                    }
                )
            label = label + 1

        dicts = json.dumps(dicts, ensure_ascii=False).encode('utf8')
        with open("/code/application/static/layers/clusters.json", 'w') as fp:
            fp.write(dicts.decode())
        return False
    except Exception as e:
        print("Exceção em create cluster layer: ", e)
        return True


def create_stop_layer(stops):
    from application.models import Stop
    try:
        dicts = {
            "type": "FeatureCollection",
            "features": []
        }
        session = []
        for cluster in stops:
            passengers = list()
            for s in cluster:
                nearest_id = s['nearest_stop']['id']
                nearest = Stop.objects.get(pk=nearest_id)
                dicts['features'].append({
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [nearest.address.coordinates.longitude, nearest.address.coordinates.latitude]
                    },
                    "properties": {
                        "type": "pickup"
                    }
                })
                passengers.append({
                    "passenger": 42,
                    "origin": {
                        "latitude": s['latitude'],
                        "longitude": s['longitude']
                    },
                    "destination": {
                        "latitude": 0.0,
                        "longitude": 0.0
                    },
                    "pickup": {
                        "id": nearest_id,
                        "distance": s['nearest_stop']['distance'],
                        "coordinates": {
                            "latitude": nearest.address.coordinates.latitude,
                            "longitude": nearest.address.coordinates.longitude
                        }
                    },
                    "dropoff": {
                        "id": 0,
                        "distance": 0,
                        "coordinates": {
                            "latitude": 0.0,
                            "longitude": 0.0
                        }
                    }
                })

            session.append(passengers)

        dicts = json.dumps(dicts, ensure_ascii=False).encode('utf8')
        with open("/code/application/static/layers/stop-route.json", 'w') as fp:
            fp.write(dicts.decode())
        return session
    except Exception as e:
        print("Exceção em create stop cluster layer: ", e)
        return True


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

