from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import ModelEvaluationArtifact
from sklearn.metrics import f1_score
from src.exception import CustomException
from src.constants import TARGET_COLUMN
from src.logger import logging
from src.utils.main_utils import load_object
import sys
import pandas as pd
from typing import Optional
from src.entity.s3_estimator import Proj1Estimator
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

@dataclass
class EvaluateModelResponse:
    trained_model_f1_score: float
    best_model_f1_score: float
    is_model_accepted: bool
    difference: float

class ModelEvaluation:
    def __init__(self):
        try:
            self.model_evaluation_config = ModelEvaluationConfig()
            self.data_transformation = DataTransformation()
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_best_model_obj(self):
        try:
            bucket_name = self.model_evaluation_config.bucket_name
            model_path = self.model_evaluation_config.s3_model_path

            proj1_estimator = Proj1Estimator(bucket_name,model_path)
            if proj1_estimator.is_model_present():
                return proj1_estimator
            
            return None
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def evaluate_model(self,data_ingestion_artifacts,model_trainer_artifacts):
        try:
            test_df = pd.read_csv(data_ingestion_artifacts.test_df_file_path)
            x , y = test_df.drop(TARGET_COLUMN, axis = 1) , test_df[TARGET_COLUMN]

            x = self.data_transformation._map_gender_column(x)
            x = self.data_transformation._drop_id_column(x)
            x = self.data_transformation._create_dummy_columns(x)
            x= self.data_transformation._rename_columns(x)

            trained_model = load_object(model_trainer_artifacts.trained_model_file_path)
            logging.info("Trained model loaded/exists.")
            trained_model_f1_score = model_trainer_artifacts.metric_artifact.f1_score
            logging.info("F1_Score for this model: {}".format(trained_model_f1_score))

            best_model_f1_score = 0
            best_model = self.get_best_model_obj()

            if best_model is not None:
                logging.info("Computing F1_Score for production model..")
                y_hat_best_model = best_model.predict(x)
                best_model_f1_score = f1_score(y,y_hat_best_model)
                logging.info(f"F1_Score-Production Model: {best_model_f1_score}, F1_Score-New Trained Model: {trained_model_f1_score}")

            result = EvaluateModelResponse(
                                            trained_model_f1_score=trained_model_f1_score,
                                            best_model_f1_score=best_model_f1_score,
                                            is_model_accepted= trained_model_f1_score > best_model_f1_score,
                                            difference= trained_model_f1_score - best_model_f1_score    
                                            )
            logging.info(f"Result: {result}")
            return result
        except Exception as e:
            raise CustomException(e,sys)
        
    def init_model_evaluation(self,data_ingestion_artifacts,model_trainer_artifacts):
        try:
            print("------------------------------------------------------------------------------------------------")
            logging.info("Initialized Model Evaluation Component.")
            evaluate_model_response = self.evaluate_model(data_ingestion_artifacts,model_trainer_artifacts)

            model_evaluation_artifact = ModelEvaluationArtifact(
                                                                is_model_accepted = evaluate_model_response.is_model_accepted,
                                                                changed_accuracy = evaluate_model_response.difference,
                                                                s3_model_path = self.model_evaluation_config.s3_model_path,
                                                                trained_model_path = model_trainer_artifacts.trained_model_file_path
                                                                )
            logging.info("Model evaluation artifact: {}".format(model_evaluation_artifact))
            return model_evaluation_artifact
            
        except Exception as e:
            raise CustomException(e,sys)
