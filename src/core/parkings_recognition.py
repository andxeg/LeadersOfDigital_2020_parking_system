import random
import numpy as np
import pandas as pd
import catboost as cb
from sklearn import preprocessing


from config import MODEL_WEIGTHS_PATH


class RecognitionModel:
    def __init__(self):
        pass

    def get_random_total(self):
        """
            For test only
        """
        return random.randint(10,20)

    def get_random_free(self):
        """
            For test only
        """
        return random.randint(5,10)

    def predict(self, photo):
        """
            For test only
        """
        
        return self.get_random_total(), self.get_random_free()

    def fit(self):
        # load model weights from MODEL_WEIGTHS_PATH
        return


def prepare_model():
    model = RecognitionModel()
    model.fit()
    return model
