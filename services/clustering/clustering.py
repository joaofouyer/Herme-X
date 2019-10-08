import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.datasets.samples_generator import make_blobs


class Clustering:
    def primary_dbscan(self, p):
        try:
            p = np.asarray(p, dtype=np.float32)
            db = DBSCAN(eps=0.0001, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(p))
            cluster_labels = db.labels_
            num_clusters = len(set(cluster_labels))
            clusters = pd.Series([p[cluster_labels == n] for n in range(num_clusters)])

            clusters = [c.tolist() for c in clusters.tolist()]

            return {
                "num_clusters": num_clusters,
                "labels": cluster_labels.tolist(),
                "clusters": clusters
            }
        except Exception as e:
            print("Exception on clustering primary_dbscan: {} {}".format(type(e), e))
            raise e

    def generate(self, center, samples):
        try:
            center = [center]
            p, labels_true = make_blobs(n_samples=samples, centers=center, cluster_std=0.002, random_state=0)
            return p
        except Exception as e:
            print("Exception on clustering generate: {} {}".format(type(e), e))
            raise e
