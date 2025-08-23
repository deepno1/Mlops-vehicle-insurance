import sys
import pandas as pd
import numpy as np
from typing import Optional
from src.exception import CustomException
from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import collection_name

class Proj1Data:

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient()
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_collection_as_dataframe(self):
        try:
            collection = self.mongo_client.database[collection_name]

            print("Fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fecthed with len: {len(df)}")
            
            if '_id' in df.columns.to_list():
                df = df.drop(columns=['_id'],axis=1)
            df.replace({'na' : np.nan},inplace = True)

            return df
        
        except Exception as e:
            raise CustomException(e,sys)
