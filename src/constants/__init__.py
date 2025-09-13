import os
from datetime import date

# For MongoDB connection
DB_NAME = 'proj1'
collection_name = 'proj1_data'
MONGODB_URL_KEY = "MONGODB_URL"


PIPELINE_NAME = ''
ARTIFACT_DIR = 'artifacts'


DATA_INGESTION_DIR = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE = 'feature_store'
DATA_INGESTED = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.25


FILE_NAME = 'data.csv'
TRAIN_DF = 'train.csv'
TEST_DF = 'test.csv'
TARGET_COLUMN = "Response"


DATA_VALIDATION_DIR = 'data_validation'
VALIDATION_REPORT_FILE = 'validation_report'


SCHEMA_FILE_PATH = os.path.join('config','schema.yaml')


DATA_TRANSFORMATION_DIR = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'transformed_data'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_object'
PREPROCESSING_OBJECT_FILE = 'preprocessing.pkl'


MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 300
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 8
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 3
MIN_SAMPLES_SPLIT_CRITERION: str = 'gini'
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101


AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "my-mlopsproj-model1"
MODEL_FILE_NAME = "model.pkl"