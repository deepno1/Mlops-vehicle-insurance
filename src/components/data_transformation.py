from src.exception import CustomException
import sys
from src.entity.config_entity import DataTransformationConfig
from src.logger import logging
from src.constants import *
from src.utils.main_utils import read_yaml_file
import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from imblearn.combine import SMOTEENN
import numpy as np
from src.utils.main_utils import save_numpy_array_data,save_object
from src.entity.artifact_entity import DataTransformationArtifacts

class DataTransformation:
    def __init__(self):
        try:
            self.data_transformation_config = DataTransformationConfig()
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)
        
    def _map_gender_column(self,df):
        logging.info("Mapping 'Gender' column to binary values")
        df['Gender'] = df['Gender'].map({'Female': 0, 'Male' : 1}).astype(int)
        return df
    
    def _create_dummy_columns(self,df):
        logging.info("Creating dummy variables for categorical features")
        df = pd.get_dummies(df, drop_first = True)
        return df
    
    def _rename_columns(self,df):
        logging.info("Renaming specific columns and casting to int")
        df = df.rename(columns={
            "Vehicle_Age_< 1 Year": "Vehicle_Age_lt_1_Year",
            "Vehicle_Age_> 2 Years": "Vehicle_Age_gt_2_Years"
        })

        for col in ["Vehicle_Age_lt_1_Year", "Vehicle_Age_gt_2_Years", "Vehicle_Damage_Yes"]:
            if col in df.columns:
                df[col] = df[col].astype('int')
        return df
    
    def _drop_id_column(self,df):
        logging.info("Dropping 'id' column")
        col = self._schema_config['drop_columns']
        if col in df.columns:
            df = df.drop(columns = [col], axis = 1)
        return df
        
    def get_data_transformer_object(self):
        try:

            num_cols = self._schema_config['num_features']
            mm_cols = self._schema_config['mm_columns']
            logging.info("Cols loaded from schema.")

            num_custom_transformer = Pipeline([
                ('StandardScaler',StandardScaler())
            ])

            mm_custom_transformer = Pipeline([
                ('MinMax',MinMaxScaler())
            ])

            preprocesser = ColumnTransformer([
                ('num_transform',num_custom_transformer,num_cols),
                ('mm_transformer',mm_custom_transformer,mm_cols)
            ],remainder='passthrough')

            logging.info("Final Pipeline Ready!!")
            logging.info("Exited get_data_transformer_object method of DataTransformation class")

            return preprocesser
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def read_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e, sys)
        
    def init_data_transformation(self,data_validation_artifacts,data_ingestion_artifacts):
        try:
            logging.info("Data Transformation Started !!!")
            if not data_validation_artifacts.validation_status:
                raise Exception(data_validation_artifacts.message)
            

            train_df , test_df = (
                DataTransformation.read_data(data_ingestion_artifacts.train_df_file_path),
                DataTransformation.read_data(data_ingestion_artifacts.test_df_file_path)
            )
            logging.info("Train-Test data loaded")


            input_feature_train_df = train_df.drop(columns = [TARGET_COLUMN], axis = 1)
            target_feature_train_df = train_df[TARGET_COLUMN]

            input_feature_test_df = test_df.drop(columns = [TARGET_COLUMN], axis = 1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            logging.info("Input and Target cols defined for both train and test df.")


            input_feature_train_df = self._map_gender_column(input_feature_train_df)
            input_feature_train_df = self._drop_id_column(input_feature_train_df)
            input_feature_train_df = self._create_dummy_columns(input_feature_train_df)
            input_feature_train_df = self._rename_columns(input_feature_train_df)

            input_feature_test_df = self._map_gender_column(input_feature_test_df)
            input_feature_test_df = self._drop_id_column(input_feature_test_df)
            input_feature_test_df = self._create_dummy_columns(input_feature_test_df)
            input_feature_test_df = self._rename_columns(input_feature_test_df)
            logging.info("Custom transformations applied to train and test data")
            

            logging.info("Starting data transformation")
            preprocesser = self.get_data_transformer_object()
            logging.info("Got the preprocessor object")

            logging.info("Initializing transformation for Training-data")
            input_feature_train_arr = preprocesser.fit_transform(input_feature_train_df)
            logging.info("Initializing transformation for Testing-data")
            input_feature_test_arr = preprocesser.transform(input_feature_test_df)
            logging.info("Transformation done end to end to train-test df.")

            logging.info("Applying SMOTEENN for handling imbalanced dataset.")
            smt = SMOTEENN(sampling_strategy="minority")
            input_feature_train_arr,target_feature_train_df = smt.fit_resample(input_feature_train_arr,target_feature_train_df)
            input_feature_test_arr,target_feature_test_df = smt.fit_resample(input_feature_test_arr,target_feature_test_df)
            logging.info("SMOTEENN applied to train-test df.")

            train_arr = np.c_[input_feature_train_arr,target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr,target_feature_test_df]
            logging.info("feature-target concatenation done for train-test df.")

            save_object(self.data_transformation_config.transformed_object_file_path,preprocesser)
            save_numpy_array_data(self.data_transformation_config.transformed_train_df_file_path,train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_df_file_path,test_arr)

            logging.info("Saving transformation object and transformed files.")

            logging.info("Data transformation completed successfully")
            return DataTransformationArtifacts(
                self.data_transformation_config.transformed_object_file_path,
                self.data_transformation_config.transformed_train_df_file_path,
                self.data_transformation_config.transformed_test_df_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
    