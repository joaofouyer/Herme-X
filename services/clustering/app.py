import falcon
import requests
from json import loads, dumps
from clustering import *
from settings.conf import LOCATION_URL
from requests.utils import get_unicode_from_response


class ClusteringService:
    def on_get(self, request, response, generate=None):
        try:
            response.status = falcon.HTTP_200

            cl = Clustering()
            data = loads(request.stream.read())
            if generate:
                coordinates = cl.generate(center=data['center'], samples=data['samples'])
                resp = []
                for c in coordinates:
                    lat, lng = c[0], c[1]
                    r = requests.get("{url}/geocoder/latlng={lat},{lng}".format(url=LOCATION_URL, lat=lat, lng=lng))
                    resp.append(loads(get_unicode_from_response(r)))
            else:
                resp = cl.primary_dbscan(p=data['coordinates'])
            response.body = dumps(resp)

        except Exception as e:
            print("Exception on ClusteringService: {} {}".format(type(e), e))
            raise e


api = falcon.API()

clustering = ClusteringService()

api.add_route('/', clustering)
api.add_route('/{generate}', clustering)
