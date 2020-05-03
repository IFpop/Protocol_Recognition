from agreement_recongizer.data_processor import PcapPreprocessor
from agreement_recongizer.data_processor import dataset_preprocessor
from agreement_recongizer.cluster import KMeansCluster
from sklearn import preprocessing
import pandas as pd

if __name__ == '__main__':
    preprocessor = PcapPreprocessor()
    dataset = pd.read_csv('data/demo_all.csv')
    dataset = dataset_preprocessor(dataset)
    cluster = KMeansCluster(dataset)
    cluster.find_best_k(range(50, 60))
