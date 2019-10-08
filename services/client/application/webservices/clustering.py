import json
import requests
from requests.utils import get_unicode_from_response
from django.conf import settings


def generate_locations(center, samples=15):
    try:
        url = "{url}/generate".format(url=settings.CLUSTERING_URL)
        response = requests.get(url, json={"center": center, "samples": samples})
        return json.loads(get_unicode_from_response(response))
    except Exception as e:
        print("Exception on generate locations: {} {}".format(type(e), e))
        raise e


def cluster_passengers(coordinates):
    try:
        url = "{url}/".format(url=settings.CLUSTERING_URL)
        response = requests.get(url, json={"coordinates": coordinates})
        return json.loads(get_unicode_from_response(response))
    except Exception as e:
        print("Exception on generate locations: {} {}".format(type(e), e))
        raise e
