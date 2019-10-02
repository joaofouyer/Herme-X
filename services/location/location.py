from coordinates import Coordinates
import json
from requests.utils import get_unicode_from_response

class Location:

    def __init__(self, street, street_number, info, neighborhood, city, state, country, zip_code, coordinates,
                 zone=None):

        self.street = street
        self.street_number = street_number
        self.info = info
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.coordinates = coordinates
        self.zone = zone

    @staticmethod
    def handler(dictionary, provider=None):
        try:
            if isinstance(dictionary, dict):
                coordinates = Coordinates.handler(dictionary=dictionary)
                zone = None
                info = None

                if provider == "bing":
                    address = dictionary.get("street")
                    if isinstance(address, str):
                        street = address.split(',')[0]
                        street_number = [int(s) for s in address.split() if s.isdigit()]
                        street_number = street_number[0] if len(street_number) else None
                    elif isinstance(dictionary.get("address"), str):
                        address = dictionary.get("address")
                        street = address.split(',')[0]
                        street_number = [int(s) for s in address.split() if s.isdigit()]
                        street_number = street_number[0] if len(street_number) else None
                    info = dictionary.get("info", None)
                    if "neighborhood" in dictionary:
                        neighborhood = dictionary.get("neighborhood")
                    else:
                        neighborhood = dictionary['raw']['address']['formattedAddress'].split(',')[1]
                        neighborhood = neighborhood.split(' - ')[1]
                    city = dictionary.get("city", None)
                    state = dictionary.get("state", None)
                    country = dictionary.get("country", None)
                    zip_code = dictionary.get("postal", None)

                elif provider == "here":
                    address = dictionary.get("address")
                    if 'street' in dictionary:
                        street = dictionary['street']

                    if 'housenumber' in dictionary:
                        street_number = int(dictionary['housenumber'])

                    elif isinstance(address, str):
                        street = address.split(',')[0]
                        street_number = [int(s) for s in address.split() if s.isdigit()]
                        street_number = street_number[0] if len(street_number) else None
                    city = dictionary.get("city")
                    country = dictionary.get("country")
                    neighborhood = dictionary.get("neighborhood")
                    zip_code = dictionary.get("postal")
                    state = dictionary['raw']['Address']['State']

                elif provider == "mapbox":
                    city = dictionary.get("city")
                    country = dictionary.get("country")
                    street_number = dictionary.get("housenumber")
                    zip_code = dictionary.get("postal")
                    street = dictionary['raw']['text']
                    neighborhood = dictionary['raw']['locality']
                    state = dictionary['state']

                elif provider == "mapquest":
                    street = dictionary.get("street")
                    city = dictionary.get("city")
                    country = dictionary.get("country")
                    zip_code = dictionary.get("postal")
                    street_number = None
                    neighborhood = None
                    state = dictionary.get("state")

                elif provider == "google":
                    street = dictionary.get("street")
                    city = dictionary.get("county")
                    country = dictionary.get("country")
                    zip_code = dictionary.get("postal")
                    street_number = dictionary.get("housenumber")
                    neighborhood = dictionary.get("sublocality")
                    state = dictionary.get("state")
                    info = dictionary.get("place")

                elif provider == "locationiq":
                    address = dictionary.get("address")
                    info = dictionary.get("display_name")
                    if isinstance(address, str):
                        street = dictionary.get("street")
                        city = dictionary.get("city")
                        country = dictionary.get("country")
                        zip_code = dictionary.get("postal")
                        street_number = dictionary.get("house_number")
                        neighborhood = dictionary.get("district")
                        state = dictionary.get("state")
                    else:
                        street = address.get("road")
                        city = address.get("city")
                        country = address.get("country")
                        zip_code = address.get("postcode")
                        street_number = address.get('house_number')
                        neighborhood = address.get('city_district')
                        state = address.get("state")

                elif provider == "arcgis":
                    address = dictionary.get("address")
                    quality = dictionary.get("quality")
                    if quality == "StreetAddress":
                        a = address.split(',')
                        street = a[0]
                        street_number = [int(s) for s in street.split() if s.isdigit()]
                        street_number = street_number[0] if len(street_number) else None
                        neighborhood = a[1]
                        city = a[2]
                        zip_code = a[3]
                    country = "BR"
                    state = "SP"

                elif provider == "opencage":
                    street = dictionary.get("path")
                    city = dictionary.get("city")
                    country = dictionary.get("country")
                    zip_code = dictionary.get("postal")
                    street_number = None
                    neighborhood = dictionary.get("neighbourhood")
                    state = dictionary.get("state")

                if isinstance(street_number, str):
                    street_number = int(street_number)
                return Location(
                    street=street, street_number=street_number, info=info, neighborhood=neighborhood,
                    city=city, state=state, country=country, zip_code=zip_code, coordinates=coordinates, zone=zone
                )
            return None

        except Exception as e:
            print("Exception on Location Handler: ", e)
            return None

    def json(self):
        return {
            "street":  self.street,
            "street_number": self.street_number,
            "info": self.info,
            "neighborhood": self.neighborhood,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "zip_code": self.zip_code,
            "coordinates": self.coordinates.json(),
            "zone": None
        }
