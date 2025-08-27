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