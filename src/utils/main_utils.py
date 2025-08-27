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
    
def save_numpy_array_data(file_path,array):
    try:
        dir = os.path.dirname(file_path)
        os.makedirs(dir, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, array)
    except Exception as e:
        raise CustomException(e, sys) 
    
def save_object(file_path: str, obj: object):
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj, file)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path: str):
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        return obj
    except Exception as e:
        raise CustomException(e, sys) 
    
def load_numpy_array_data(file_path: str):
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys) 