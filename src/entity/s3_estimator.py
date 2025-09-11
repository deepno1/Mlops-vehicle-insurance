import sys
from src.exception import CustomException
from src.cloud_storage.aws_storage import SimpleStorageService
from pandas import DataFrame
from src.constants import *

class Proj1Estimator:
    def __init__(self,bucket_name,model_path):
        try:
            self.bucket_name = bucket_name
            self.model_path = model_path
            self.s3 = SimpleStorageService()

        except Exception as e:
            raise CustomException(e,sys)
        
    def is_model_present(self):
        try:
            return self.s3.s3_key_path_available(self.bucket_name,self.model_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def load_model(self):
        try:
            return self.s3.load_model(self.bucket_name,self.model_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def predict(self,df):
        try:
            model = self.load_model()
            return model.predict(df)
        except Exception as e:
            raise CustomException(e,sys)


