import boto3
from src.configuration.aws_connection import S3Client
from io import StringIO
from typing import Union,List
import os,sys
from src.logger import logging
from mypy_boto3_s3.service_resource import Bucket
from src.exception import CustomException
from botocore.exceptions import ClientError
from pandas import DataFrame,read_csv
import pickle

class SimpleStorageService:
    def __init__(self):
        try:
            s3_client = S3Client()
            self.s3_resource = s3_client.s3_resource
            self.s3_client = s3_client.s3_client

        except Exception as e:
            raise CustomException(e,sys)
        
    def get_bucket(self,bucket_name):
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            logging.info("Exited the get_bucket method of SimpleStorageService class")
            return bucket
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def s3_key_path_available(self,bucket_name,model_path):
        try :
            bucket = self.get_bucket(bucket_name)
            file_objs = [obj for obj in bucket.objects.filter(Prefix = model_path)]
            return len(file_objs) > 0
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_objects(self,bucket_name,model_path):
        logging.info("Entered the get_objects method of SimpleStorageService class")
        try:
            bucket = self.get_bucket(bucket_name)
            file_objs = [obj for obj in bucket.objects.filter(Prefix = model_path)]
            func = lambda x:x[0] if len(x) == 1 else x
            file_objs = func(file_objs)
            logging.info("Exited the get_file_object method of SimpleStorageService class")
            return file_objs

        except Exception as e:
            raise CustomException(e,sys)
        
    def read_object(self,file_object,decode : bool = True, make_readable : bool = False):
        try :
            if decode == True:
                if make_readable == True:
                    content = StringIO(file_object.get()['Body'].read().decode())
                else:
                    content = file_object.get()['Body'].read().decode()
            else:
                content = file_object.get()['Body'].read()
            return content
        except Exception as e:
            raise CustomException(e,sys)
        
    def load_model(self,bucket_name,model_path):
        try:
            file_objects = self.get_objects(bucket_name,model_path)
            model_obj_file = self.read_object(file_objects,decode = False)
            model = pickle.loads(model_obj_file)
            logging.info("Production model loaded from S3 bucket.")
            return model
        except Exception as e:
            raise CustomException(e,sys)
        
    def upload_file(self,from_file,bucket_name,to_filename,remove : bool = False):
        try:
            logging.info(f"Uploading {from_file} to {to_filename} in {bucket_name}")
            self.s3_resource.meta.client.upload_file(from_file,bucket_name,to_filename)
            logging.info(f"Uploaded {from_file} to {to_filename} in {bucket_name}")

            if remove:
                os.remove(from_file)
                logging.info(f"Removed local file {from_file} after upload")
            logging.info("Exited the upload_file method of SimpleStorageService class")

        except Exception as e:
            raise CustomException(e,sys)
