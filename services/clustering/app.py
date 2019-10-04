import falcon
import json
from itertools import permutations
from datetime import datetime, timedelta
import numpy as np
from math import fabs
from sklearn.cluster import DBSCAN
from sklearn.neighbors import DistanceMetric
from scipy.spatial.distance import pdist, squareform


class Clustering:
    def cluster(self):
        try:
            classifier = DBSCAN(eps=7, min_samples=1, metric="precomputed")
            return None
        except Exception as e:
            print("Clustering exception {} {}".format(type(e), e))
            raise e

    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        quotes = {"quote": "Two things awe me most, the starry sky above me and the moral law within me.",
                  "author": "Immanuel Kant"}
        response.body = json.dumps(quotes)


api = falcon.API()
clustering = Clustering()
api.add_route('/', clustering)
