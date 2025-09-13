from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    train_df_file_path : str
    test_df_file_path : str

@dataclass
class DataValidationArtifacts:
    validation_status : bool
    message : str
    validation_report_file_path : str

@dataclass
class DataTransformationArtifacts:
    transformed_obj_file_path : str
    transformed_train_arr_file_path : str
    transformed_test_arr_file_path : str

@dataclass
class ClassificationMetricArtifact:
    f1_score : float
    precision_score : float
    recall_score : float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path : str 
    metric_artifact : ClassificationMetricArtifact

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted : bool
    changed_accuracy : float
    s3_model_path : str 
    trained_model_path : str

@dataclass
class ModelPusherArtifact:
    bucket_name: str 
    s3_model_path: str 