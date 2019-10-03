import json
import geocoder
import requests
import falcon
from requests.utils import get_unicode_from_response

from settings.conf import FOWARD_PROVIDERS, REVERSE_PROVIDERS, OPENCAGE_KEY, LOCATIONIQ_KEY, MAPBOX_KEY, MAPQUEST_KEY,\
    BING_KEY, GOOGLE_GEOCODING, HERE_ID, HERE_CODE
from models.location import Location


class Geocoding:
    def __init__(self):
        self.provider = None
        self.address = None
        self.latlng = None
        self.coord = [self.latlng]

    def arcgis(self):
        return geocoder.arcgis(self.address)

    def bing(self):
        return geocoder.bing(self.address, key=BING_KEY, countryRegion='BR')

    def here(self):
        return geocoder.here(self.address, app_id=HERE_ID, app_code=HERE_CODE)

    def mapbox(self):
        return geocoder.mapbox(self.address, key=MAPBOX_KEY)

    def mapquest(self):
        return geocoder.mapquest(self.address, key=MAPQUEST_KEY)

    def locationiq(self):
        return geocoder.locationiq(self.address, key=LOCATIONIQ_KEY)

    def google(self):
        return geocoder.google(self.address, key=GOOGLE_GEOCODING, components="country:BR")

    def opencage(self):
        return geocoder.opencage(self.address, key=OPENCAGE_KEY)

    def reverse_here(self):
        return geocoder.here(self.coord, method='reverse', app_id=HERE_ID, app_code=HERE_CODE)

    def reverse_bing(self):
        return geocoder.bing(self.coord, method='reverse', key=BING_KEY)

    def reverse_locationiq(self):
        url = "https://us1.locationiq.com/v1/reverse.php"
        data = {
            'key': LOCATIONIQ_KEY,
            'lat': self.coord[0],
            'lon': self.coord[1],
            'format': 'json'
        }
        response = requests.get(url, params=data)

        return json.loads(get_unicode_from_response(response))

    def reverse_mapquest(self):
        return geocoder.mapquest(self.coord, method='reverse', key=MAPQUEST_KEY)

    def reverse_mapbox(self):
        return geocoder.mapbox(self.coord, method='reverse', key=MAPBOX_KEY)

    def reverse_google(self):
        return geocoder.google(self.coord, method='reverse', key=GOOGLE_GEOCODING)

    def foward(self, fallback=0):
        try:
            if fallback > 7:
                raise falcon.HTTPBadGateway(description="All reverse geocoding services are unavailable.")
            providers = {
                "arcgis": self.arcgis,
                "bing": self.bing,
                "here": self.here,
                "mapbox": self.mapbox,
                "mapquest": self.mapquest,
                "locationiq": self.locationiq,
                "google": self.google,
                "opencage": self.opencage,
            }

            g = providers.get(self.provider)
            if g is not None:
                geocoded = g()
                if geocoded.ok:
                    geocoded = Location.handler(dictionary=geocoded.json, provider=self.provider)
                    if isinstance(geocoded, Location):
                        return geocoded

            self.provider = FOWARD_PROVIDERS[fallback]
            return self.foward(fallback=fallback + 1)

        except Exception as e:
            print("Exception on foward geocoding: ", e)
            return None

    def reverse(self, fallback=0):
        try:
            if fallback > 5:
                raise falcon.HTTPBadGateway(description="All reverse geocoding services are unavailable.")
            providers = {
                "here": self.reverse_here,
                "bing": self.reverse_bing,
                "locationiq": self.reverse_locationiq,
                "mapquest": self.reverse_mapquest,
                "mapbox": self.reverse_mapbox,
                "google": self.reverse_google,
            }

            loc = providers.get(self.provider)

            if loc is not None:
                geocoded = loc()
                if self.provider == "locationiq":
                    geocoded = Location.handler(dictionary=geocoded, provider=self.provider)
                    if isinstance(geocoded, Location):
                        return geocoded
                elif geocoded.ok:
                    geocoded = Location.handler(dictionary=geocoded.json, provider=self.provider)
                    if isinstance(geocoded, Location):
                        return geocoded

            self.provider = REVERSE_PROVIDERS[fallback]
            return self.reverse(fallback=fallback + 1)
        except Exception as e:
            print("Exception on reverse geocoding: ", e)
            return None
