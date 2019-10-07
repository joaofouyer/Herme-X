def do():
    try:
        print(__doc__)
        import numpy as np
        from sklearn.cluster import DBSCAN
        from sklearn import metrics
        from sklearn.datasets.samples_generator import make_blobs
        from sklearn.preprocessing import StandardScaler

        # #############################################################################
        # Generate sample data
        centers = [[1, 1], [-1, -1], [1, -1]]
        X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                                    random_state=0)

        X = StandardScaler().fit_transform(X)

        # #############################################################################
        # Compute DBSCAN
        db = DBSCAN(eps=0.3, min_samples=10).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

        print('Estimated number of clusters: %d' % n_clusters_)
        print('Estimated number of noise points: %d' % n_noise_)
        print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
        print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
        print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
        print("Adjusted Rand Index: %0.3f"
              % metrics.adjusted_rand_score(labels_true, labels))
        print("Adjusted Mutual Information: %0.3f"
              % metrics.adjusted_mutual_info_score(labels_true, labels,
                                                   average_method='arithmetic'))
        print("Silhouette Coefficient: %0.3f"
              % metrics.silhouette_score(X, labels))

        # #############################################################################
        # Plot result
        import matplotlib.pyplot as plt

        # Black removed and is used for noise instead.
        unique_labels = set(labels)
        colors = [plt.cm.Spectral(each)
                  for each in np.linspace(0, 1, len(unique_labels))]
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = [0, 0, 0, 1]

            class_member_mask = (labels == k)

            xy = X[class_member_mask & core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=14)

            xy = X[class_member_mask & ~core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=6)

        plt.title('Estimated number of clusters: %d' % n_clusters_)
        plt.show()

    except Exception as e:
        print("Exception on example do: {} {}".format(type(e), e))
        raise e


def passengers():
    try:
        import numpy as np
        import pandas as pd
        from sklearn.cluster import DBSCAN
        from sklearn import metrics
        from sklearn.datasets.samples_generator import make_blobs
        from sklearn.preprocessing import StandardScaler

        # agrupamento dos pontos de emabarque
        center = [[-23.512099, -46.666171], [-23.534053, -46.792044]]

        # Cria n exemplos (n_samples) a partir do centro. Descobrir o que é cluster std e random state.
        # Mas o importante é que aqui será substituído pelos passageiros da base de dados.
        # FORMATO DE PASSENGERS:
        # [[-23.33455371 - 46.53270127]
        # [-23.49379559 - 46.74104454]
        # [-23.83735751 - 47.35668404]
        # [-24.19460708 - 45.88586084]
        # [-23.20768391 - 46.61750099]
        # [-23.05633873 - 47.16010133]
        # [-23.44112854 - 46.82688337]]

        passengers, labels_true = make_blobs(n_samples=15, centers=center, cluster_std=0.002, random_state=0)
        print(passengers)
        # passengers = StandardScaler().fit_transform(passengers) # Insere em uma escala parecida com do plano cartesiano.

        # #############################################################################
        # Compute DBSCAN
        db = DBSCAN(eps=0.0001, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(passengers))
        cluster_labels = db.labels_
        num_clusters = len(set(cluster_labels))
        print(cluster_labels)
        clusters = pd.Series([passengers[cluster_labels == n] for n in range(num_clusters)])
        print(clusters)
        print('Number of clusters: {}'.format(num_clusters))

    except Exception as e:
        print("Exception on clustering passengers: {} {}".format(type(e), e))
        raise e