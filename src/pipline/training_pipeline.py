import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import dataIngestion

class TrainPipeline:

    def __init__(self):
        self.data_ingestion = dataIngestion()

    def start_data_ingestion(self):
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")

            data_ingestion_artifacts = self.data_ingestion.init_data_ingestion()

            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)