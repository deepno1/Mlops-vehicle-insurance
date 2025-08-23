from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    train_df_file_path : str
    test_df_file_path : str