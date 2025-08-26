import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name : str = PIPELINE_NAME 
    artifact_dir : str = os.path.join(ARTIFACT_DIR,timestamp)
    timestamp : str = timestamp

training_Pipeline_Config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_Pipeline_Config.artifact_dir,DATA_INGESTION_DIR) 
    feature_store_file_path = os.path.join(data_ingestion_dir,DATA_INGESTION_FEATURE_STORE,FILE_NAME)
    train_df_file_path = os.path.join(data_ingestion_dir,DATA_INGESTED,TRAIN_DF)
    test_df_file_path = os.path.join(data_ingestion_dir,DATA_INGESTED,TEST_DF)
    train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    data_ingestion_collection_name = collection_name

@dataclass
class DataValidationConfig:
    data_validation_dir = os.path.join(training_Pipeline_Config.artifact_dir,DATA_VALIDATION_DIR)
    validation_report_file_path = os.path.join(data_validation_dir,VALIDATION_REPORT_FILE)
    
@dataclass
class DataTransformationConfig:
    data_transformation_dir = os.path.join(training_Pipeline_Config.artifact_dir,DATA_TRANSFORMATION_DIR)
    transformed_train_df_file_path = os.path.join(data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,TRAIN_DF.replace('csv','npy'))
    transformed_test_df_file_path = os.path.join(data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,TEST_DF.replace('csv','npy'))
    transformed_object_file_path = os.path.join(data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,PREPROCESSING_OBJECT_FILE)