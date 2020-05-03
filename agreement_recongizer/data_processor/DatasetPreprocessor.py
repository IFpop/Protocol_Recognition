from sklearn import preprocessing
import pandas as pd


def dataset_preprocessor(dataset: pd.DataFrame, mode: str = 'scale') -> pd.DataFrame:
    if mode == 'scale':
        columns = dataset.columns
        dataset = preprocessing.scale(dataset)
        dataset = pd.DataFrame(dataset, columns=columns)
        return dataset
