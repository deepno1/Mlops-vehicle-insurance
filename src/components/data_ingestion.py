import sys
from src.exception import CustomException
from src.logger import logging
import os
from pandas import DataFrame
from src.entity.config_entity import DataIngestionConfig
from src.data_access.proj_data import Proj1Data
from sklearn.model_selection import train_test_split
from src.entity.artifact_entity import DataIngestionArtifacts

class dataIngestion:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_into_feature_store(self):
        try:
            logging.info("Exporting data from mongodb")
            my_data = Proj1Data()
            dataframe = my_data.export_collection_as_dataframe()
            logging.info("Shape of dataframe: {}".format(dataframe.shape))

            dir_path = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(dir_path, exist_ok = True)
            logging.info("Saving exported data into feature store file path: {}".format(self.data_ingestion_config.feature_store_file_path))

            dataframe.to_csv(self.data_ingestion_config.feature_store_file_path,index = False,header = True)
            return dataframe

        except Exception as e:
            raise CustomException(e,sys)
        
    def split_data_as_train_test(self,dataframe : DataFrame):
        try:
            train_df,test_df = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.train_df_file_path)
            os.makedirs(dir_path , exist_ok = True)

            logging.info(f"Exporting train and test file path.")
            train_df.to_csv(self.data_ingestion_config.train_df_file_path,index = False,header = True)
            test_df.to_csv(self.data_ingestion_config.test_df_file_path,index = False,header = True)

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise CustomException(e,sys)
        
    def init_data_ingestion(self):
        try:
            df =  self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")
            self.split_data_as_train_test(df)
            logging.info("Performed train test split on the dataset")
            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")

            data_ingestion_artifacts = DataIngestionArtifacts(
                train_df_file_path= self.data_ingestion_config.train_df_file_path,
                test_df_file_path= self.data_ingestion_config.test_df_file_path
            )

            logging.info("Data ingestion artifact: {}".format(data_ingestion_artifacts))

            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e,sys)
