import sys
from src.entity.artifact_entity import ModelPusherArtifact
from src.cloud_storage.aws_storage import SimpleStorageService
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import ModelPusherConfig
from src.entity.s3_estimator import Proj1Estimator

class ModelPusher:
    def __init__(self):
        try:
            self.model_pusher_config = ModelPusherConfig()
        except Exception as e:
            raise CustomException(e,sys)
        
    def init_model_pusher(self,model_evaluation_artifacts):
        try:
            print("------------------------------------------------------------------------------------------------")
            logging.info("Entered initiate_model_pusher method of ModelPusher class") 
            logging.info("Uploading artifacts folder to s3 bucket")
            
            logging.info("Uploading new model to S3 bucket....")
            self.proj1_esrimator = Proj1Estimator(self.model_pusher_config.bucket_name,self.model_pusher_config.s3_model_path)

            self.proj1_esrimator.save_model(model_evaluation_artifacts.trained_model_path)

            model_pusher_artifact = ModelPusherArtifact(bucket_name=self.model_pusher_config.bucket_name,
                                                        s3_model_path=self.model_pusher_config.s3_model_path)

            logging.info("Uploaded artifacts folder to s3 bucket")
            logging.info(f"Model pusher artifact: [{model_pusher_artifact}]")
            logging.info("Exited initiate_model_pusher method of ModelPusher class")
            
            return model_pusher_artifact

        except Exception as e:
            raise CustomException(e,sys)