import falcon
import json
from example import *


class Clustering:
    def cluster(self):
        try:
            classifier = passengers()
            print(classifier)
            return None
        except Exception as e:
            print("Clustering exception {} {}".format(type(e), e))
            raise e

    def on_get(self, request, response):
        response.status = falcon.HTTP_200

        self.cluster()

        quotes = {"quote": "Two things awe me most, the starry sky above me and the moral law within me.",
                  "author": "Immanuel Kant"}

        response.body = json.dumps(quotes)


api = falcon.API()
clustering = Clustering()
api.add_route('/', clustering)
