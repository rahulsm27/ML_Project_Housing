from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.artifact_entity import DataValidation

from housing.exception import HousingException
from housing.logger import logging

import sys,os
import pandas as pd
import numpy as np
import sklearn

class DataValidation :

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact)
        
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_config = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        
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
                
                message = f" Training file : {training_file} or Testing file:{testing_file} is not present"
                logging.info(message)
                raise Exception(message)
        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            # Number of column
            # Check the value of ocean proximity
            # Column names

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_validation(self):
        try :
            
            is_available = self.is_train_test_file_exists()
            validation_status = self.validate_dataset_schema()
        except Exception as e:
            raise HousingException(e,sys) from e
