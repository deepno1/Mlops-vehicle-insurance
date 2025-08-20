import os
from pathlib import Path

project_name = 'src'

list_of_files = [

    "{}/__init__.py".format(project_name),
    "{}/components/__init__.py".format(project_name),
    "{}/components/data_ingestion.py".format(project_name),  
    "{}/components/data_validation.py".format(project_name),
    "{}/components/data_transformation.py".format(project_name),
    "{}/components/model_trainer.py".format(project_name),
    "{}/components/model_evaluation.py".format(project_name),
    "{}/components/model_pusher.py".format(project_name),
    "{}/configuration/__init__.py".format(project_name),
    "{}/configuration/mongo_db_connection.py".format(project_name),
    "{}/configuration/aws_connection.py".format(project_name),
    "{}/cloud_storage/__init__.py".format(project_name),
    "{}/cloud_storage/aws_storage.py".format(project_name),
    "{}/data_access/__init__.py".format(project_name),
    "{}/data_access/proj_data.py".format(project_name),
    "{}/constants/__init__.py".format(project_name),
    "{}/entity/__init__.py".format(project_name),
    "{}/entity/config_entity.py".format(project_name),
    "{}/entity/artifact_entity.py".format(project_name),
    "{}/entity/estimator.py".format(project_name),
    "{}/entity/s3_estimator.py".format(project_name),
    "{}/exception/__init__.py".format(project_name),
    "{}/logger/__init__.py".format(project_name),
    "{}/pipline/__init__.py".format(project_name),
    "{}/pipline/training_pipeline.py".format(project_name),
    "{}/pipline/prediction_pipeline.py".format(project_name),
    "{}/utils/__init__.py".format(project_name),
    "{}/utils/main_utils.py".format(project_name),
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",

]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir,exist_ok = True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
    else:
        print("{} already exists.".format(file_name))