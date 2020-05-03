from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class KMeansCluster:
    __dataset: None

    def __init__(self, dataset):
        self.__dataset = dataset

    def find_best_k(self, k_range: range = range(1, 15)) -> None:
        inertia_list_ = []
        for i in k_range:
            print('Training cluster when k = {}...'.format(i))
            cluster = KMeans(n_clusters=i)
            cluster.fit(self.__dataset)
            inertia_list_.append(cluster.inertia_)
        # Show the trend graph
        plt.plot(k_range, inertia_list_, marker='o')
        plt.xlabel('Number of clusters')
        plt.ylabel('Inertia')
        plt.show()
