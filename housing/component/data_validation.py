from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.artifact_entity import DataValidationArtifact
from housing.util.util import read_yaml_file

from housing.constant import *

from housing.exception import HousingException
from housing.logger import logging

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

import sys,os
import pandas as pd
import numpy as np
import sklearn
import json

class DataValidation :

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys)
        
    def is_train_test_file_exists(self)->bool:

        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_test_file_exist and is_train_file_exist

            logging.info(f"Is train and test file exists ? -> {is_available}")

            if not is_available:
                
                message = f" Training file : {train_file_path} or Testing file:{test_file_path} is not present"
                logging.info(message)
                raise Exception(message)
        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_config.test_file_path

            train_file_df = pd.read_csv(train_file_path)

            len(train_file_df.columns)
                
            schema_file_path = self.data_validation_config.schema_file_path
            schema_contents = read_yaml_file(schema_file_path)

            # Number of column
            # Check the value of ocean proximity
            # Column names

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[ DataDriftProfileSection()])
            train_df,test_df = self.get_train_and_test_df()
            profile.calculate(train_df,test_df)
            report= json.loads(profile.json()) 
            
            with open(self.data_validation_config.report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)

            return report
        except Exception as e:
            raise HousingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs = [DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)
            dashboard.save(self.data_validation_config.report_page_file_path)
        
        
        except Exception as e:
            raise HousingException(e,sys) from e 


    def is_data_dirft_found(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            
            return True
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self)->DataValidationArtifact:
        try :
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_dirft_found()
            # is_available = self.is_train_test_file_exists()
            # validation_status = self.validate_dataset_schema()

            data_validation_artifact =  DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                reprot_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated = True,
                message="Data Valdiation performed sucessfully"
            )

            logging.info(f"Data validation artifact :{data_validation_artifact}")

            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
