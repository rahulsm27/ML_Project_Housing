# Any helper function will be written in this file like reading yaml file, creating pickle file etc.

import yaml
from housing.exception import HousingException
import os,sys

def read_yaml_file(file_path:str)->dict:
        """
        Reads a yaml file and returns the contents as a dictionary
        file_path : str
        """

        try:
            onfig_info = None
            with open(file_path,"rb") as yaml_file:
                return yaml.safe_load(yaml_file)
            
        except Exception as e:
             raise HousingException(e,sys) from e