import sys

import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging

class MyModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        try:
            self.preprocessing_object = preprocessing_object
            self.trained_model_object = trained_model_object

        except Exception as e :
            raise CustomException(e,sys)