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
