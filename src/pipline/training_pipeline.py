import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import dataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:

    def __init__(self):
        try:
            self.data_ingestion = dataIngestion()
            self.data_validation = DataValidation()
            self.data_transformation = DataTransformation()
            self.model_trainer = ModelTrainer()
            
        except Exception as e:
            raise CustomException(e,sys)

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
        
    def start_data_validation(self,data_ingestion_artifacts):
        logging.info("Entered the start_data_validation method of TrainPipeline class")
        try:
            data_validation_artifacts =self.data_validation.init_data_validation(data_ingestion_artifacts)

            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_transformation(self,data_validation_artifacts,data_ingestion_artifacts):
        logging.info("Entered the start_data_transformation method of TrainPipeline class")
        try:
            data_transformation_artifacts = self.data_transformation.init_data_transformation(data_validation_artifacts,data_ingestion_artifacts)
            logging.info("Performed the data transformation operation")
            logging.info("Exited the start_data_transformation method of TrainPipeline class")

            return data_transformation_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_model_trainer(self, data_transformation_artifacts):
        
        try:
            
            model_trainer_artifacts = self.model_trainer.initiate_model_trainer(data_transformation_artifacts)
            return model_trainer_artifacts

        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts)
            data_transformation_artifacts = self.start_data_transformation(data_validation_artifacts,data_ingestion_artifacts)
            model_trainer_artifacts = self.start_model_trainer(data_transformation_artifacts)
        except Exception as e:
            raise CustomException(e,sys)