from src.exception import CustomException
import sys
from src.logger import logging
import os
import numpy as np
import dill
import yaml
from pandas import DataFrame

def read_yaml_file(file_path : str):
    try:
        with open(file_path,'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise CustomException(e,sys)