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