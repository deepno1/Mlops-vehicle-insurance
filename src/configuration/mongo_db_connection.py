import os
import sys
import pymongo
import certifi
from src.exception import CustomException
from src.constants import MONGODB_URL_KEY,DB_NAME
from src.logger import logging
from dotenv import load_dotenv

load_dotenv()

ca = certifi.where()

class MongoDBClient:

    client = None

    def __init__(self):
        try:
            
            if MongoDBClient.client is None:
                Mongo_url = os.getenv(MONGODB_URL_KEY)
                if Mongo_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                MongoDBClient.client = pymongo.MongoClient(Mongo_url,tlsCAFile = ca)

            self.client = MongoDBClient.client
            self.database = self.client[DB_NAME]
            self.database_name = DB_NAME
            logging.info("MongoDB connection successful.")
            
        except Exception as e:
            raise CustomException(e,sys)