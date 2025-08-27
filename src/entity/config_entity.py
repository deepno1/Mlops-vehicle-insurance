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

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_Pipeline_Config.artifact_dir, MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME)
    expected_accuracy: float = MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path: str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    _n_estimators = MODEL_TRAINER_N_ESTIMATORS
    _min_samples_split = MODEL_TRAINER_MIN_SAMPLES_SPLIT
    _min_samples_leaf = MODEL_TRAINER_MIN_SAMPLES_LEAF
    _max_depth = MIN_SAMPLES_SPLIT_MAX_DEPTH
    _criterion = MIN_SAMPLES_SPLIT_CRITERION
    _random_state = MIN_SAMPLES_SPLIT_RANDOM_STATE