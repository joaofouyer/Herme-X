import json
import requests
from tqdm import tqdm
from pprint import pprint
import re
from requests.utils import get_unicode_from_response
from django.conf import settings
from application.management.scripts import sptrans_to_json
from application.models import Coordinates, Stop, Location, Company


def import_stops():
    try:
        file = open("/code/datasets/sptrans/stops.json", mode="r")
        create_stops(json.load(file))

        return False
    except FileNotFoundError:
        stops = sptrans_to_json()
        create_stops(json.loads(stops))
    except Exception as e:
        print("Exceção {} em import_stops: {}".format(type(e), e.message))
        return True


def create_stops(stops):
    try:
        errors = []
        incomplete = []
        cc = Coordinates(
            latitude=-23.545584,
            longitude=-46.633164
        )
        ll = Location(
            street='Rua Boa Vista',
            street_number=236,
            neighborhood='Centro',
            city='São Paulo',
            state='SP',
            country='BR',
            zip_code='01014-000',
            coordinates=cc
        )
        sptrans = Company.objects.filter(name="SPTrans").first()
        for stop in tqdm(stops):

            response = requests.get("{url}/geocoder/latlng={lat},{lng}".format(
                url=settings.LOCATION_URL,
                lat=stop['address']['coordinates']['latitude'],
                lng=stop['address']['coordinates']['longitude'])
            )

            if response.status_code == 200:
                response = json.loads(get_unicode_from_response(response))
                coordinates = Coordinates(
                    latitude=stop['address']['coordinates']['latitude'],
                    longitude=stop['address']['coordinates']['longitude']
                )

                coordinates.save()
                if 'raw' in response:
                    if 'locality' in response['raw']:
                        neighborhood = response['raw']['locality']
                    else:
                        neighborhood = 'N/A'
                        incomplete.append({'id': stop['id'], 'field': 'neighborhood'})
                    if 'text' in response['raw']:
                        street = response['raw']['text']
                    else:
                        street = 'N/A'
                        incomplete.append({'id': stop['id'], 'field': 'street'})
                else:
                    street = 'N/A'
                    neighborhood = 'N/A'
                    incomplete.append({'id': stop['id'], 'field': 'neighborhood'})
                    incomplete.append({'id': stop['id'], 'field': 'street'})

                if 'housenumber' in response:
                    housenumber = re.sub("\D", "", response['housenumber'])

                else:
                    housenumber = 0
                    incomplete.append({'id': stop['id'], 'field': 'housenumber'})

                if 'city' in response:
                    city = response['city']
                else:
                    city = 'N/A'
                    incomplete.append({'id': stop['id'], 'field': 'city'})
                if 'state' in response:
                    state = response['state']
                else:
                    state = 'SP'
                    incomplete.append({'id': stop['id'], 'field': 'state'})
                if 'country' in response:
                    country = response['country']
                else:
                    country = 'BR'
                    incomplete.append({'id': stop['id'], 'field': 'country'})
                if 'postal' in response:
                    postal = response['postal']
                else:
                    postal = 'N/A'
                    incomplete.append({'id': stop['id'], 'field': 'postal'})
                location = Location(
                    coordinates=coordinates,
                    street=street,
                    street_number=housenumber,
                    info="Parada SPTrans",
                    neighborhood=neighborhood,
                    city=city,
                    state='SP',
                    country='BR',
                    zip_code=postal,
                )
                location.save()
                if 'reference' in stop and stop['reference']:
                    reference = stop['reference']
                else:
                    reference = location.street
                stop = Stop(
                    address=location,
                    reference=stop['reference'],
                    company=sptrans
                ).save()
            else:
                errors.append(stops[0])
        print(errors)
        print(incomplete)
        return False
    except Exception as e:
        print("Exceção {} em import_stops: {}".format(type(e), e))
        return True