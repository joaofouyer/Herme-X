import json
import requests
from requests.utils import get_unicode_from_response
from django.conf import settings


def sync(mode, data):
    try:
        if len(data) > 1000:
            remaining = len(data)
            start, end = 0, 1000
            remaining = remaining - end
            chunk = data[start:end]
            while remaining:
                response = requests.post("{url}/sync/{mode}".format(url=settings.LOCATION_URL, mode=mode), json=chunk)
                if response.status_code == 200:
                    start = end
                    if remaining > 1000:
                        end = end + 1000
                        remaining = remaining - 1000
                    else:
                        end + remaining
                        remaining = 0
                    chunk = data[start:end]
                else:
                    return True

        else:
            response = requests.post("{url}/sync/{mode}".format(url=settings.LOCATION_URL, mode=mode), json=data)
            if response.status_code == 200:
                response = json.loads(get_unicode_from_response(response))
                print(response)
                return None

    except Exception as e:
        print("Exception on location webservice sync: {} {}".format(type(e), e))
        raise e


def find_nearest_stop(passengers):
    try:
        url = "{url}/find-stop".format(url=settings.LOCATION_URL)
        response = requests.get(url, json=passengers)
        return json.loads(get_unicode_from_response(response))
    except Exception as e:
        print("Exception on get nearest stop: {} {}".format(type(e), e))
        raise e


def get_distance(origin, destination):
    try:
        origin = "{lat}{lng}".format(lat=origin[0], lng=origin[1])
        destination = "{lat}{lng}".format(lat=destination[0], lng=destination[1])
        url = "{url}/distance/origin={origin}&destination={destination}".format(
            url=settings.LOCATION_URL,
            origin=origin,
            destination=destination
        )
        response = requests.get(url)
        return json.loads(get_unicode_from_response(response))
    except Exception as e:
        print("Exception on get_distance: {} {}".format(type(e), e))
        raise e


def sort_places(places):
    try:
        url = "{url}/distance/sort".format(url=settings.LOCATION_URL)
        response = requests.get(url, json=places)
        return json.loads(get_unicode_from_response(response))
    except Exception as e:
        print("Exception on sort_places: {} {}".format(type(e), e))
        raise e
