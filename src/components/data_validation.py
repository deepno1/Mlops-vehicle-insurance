from src.exception import CustomException
import sys
from src.logger import logging
from src.constants import *
from src.entity.config_entity import DataValidationConfig
from src.utils.main_utils import read_yaml_file
from pandas import DataFrame
import pandas as pd
import json
from src.entity.artifact_entity import DataValidationArtifacts

class DataValidation:
    def __init__(self):
        try:
            self.data_validation_config = DataValidationConfig()
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise CustomException(e,sys)
        
    def validate_number_of_columns(self,dataframe : DataFrame):
        try:
            status = len(dataframe.columns) == len(self._schema_config['columns'])
            logging.info("Is required column present: [{}]".format(status))
            return status
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def is_column_exist(self,dataframe : DataFrame):
        try:
            df_columns = dataframe.columns.to_list()
            missing_num_cols = []
            missing_cat_cols = []

            for col in self._schema_config['numerical_columns']:
                if col not in df_columns:
                    missing_num_cols.append(col)
            if len(missing_num_cols) > 0:
                logging.info("Missing numerical column: {}".format(missing_num_cols))

            for col in self._schema_config['categorical_columns']:
                if col not in df_columns:
                    missing_cat_cols.append(col)
            if len(missing_cat_cols) > 0:
                logging.info("Missing categorical column: {}".format(missing_cat_cols))

            return False if len(missing_cat_cols)>0 or len(missing_num_cols)>0 else True
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e, sys)
        
    def init_data_validation(self,data_ingestion_artifact):
        try:
            validation_error_msg = ''
            logging.info("Starting data validation")
            train_df , test_df = (
                DataValidation.read_data(data_ingestion_artifact.train_df_file_path),
                DataValidation.read_data(data_ingestion_artifact.test_df_file_path)
            )

            status = self.validate_number_of_columns(train_df)
            if status :
                logging.info("All required columns present in training dataframe: {}".format(status))
            else:
                validation_error_msg = validation_error_msg + 'Columns are missing in train dataframe.'

            status = self.validate_number_of_columns(test_df)
            if status :
                logging.info("All required columns present in testing dataframe: {}".format(status))
            else:
                validation_error_msg = validation_error_msg + 'Columns are missing in test dataframe.'
        

            status = self.is_column_exist(train_df)
            if status:
                logging.info("All categorical/int columns present in training dataframe: {}".format)
            else:
                validation_error_msg = validation_error_msg + 'Columns are missing in training dataframe.'
            
            status = self.is_column_exist(test_df)
            if status:
                logging.info("All categorical/int columns present in testing dataframe: {}".format)
            else:
                validation_error_msg = validation_error_msg + 'Columns are missing in testing dataframe.'

            validation_status = len(validation_error_msg) == 0

            validation_report = {
                'Validation_Status' : validation_status,
                'Message' : validation_error_msg.strip()
            } 

            dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(dir,exist_ok=True)

            with open(self.data_validation_config.validation_report_file_path,'w') as f:
                json.dump(validation_report,f,indent=4)

            logging.info("Data validation artifact created and saved to JSON file.")

            data_validation_artifacts = DataValidationArtifacts(
                validation_status= validation_status,
                message= validation_error_msg.strip(),
                validation_report_file_path= self.data_validation_config.validation_report_file_path
            )

            logging.info("Data validation artifact: {}".format(data_validation_artifacts))

            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        

