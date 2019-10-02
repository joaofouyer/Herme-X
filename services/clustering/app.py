import falcon
import json


class Clustering():
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        quotes = {"quote": "Two things awe me most, the starry sky above me and the moral law within me.",
                  "author": "Immanuel Kant"}
        response.body = json.dumps(quotes)


api = falcon.API()
clustering = Clustering()
api.add_route('/', clustering)
