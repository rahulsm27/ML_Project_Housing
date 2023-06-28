from setuptools import setup,find_packages
#from typing import List



def get_requirements_list():
    """
    Descripton : This function is going to return the list of requirment
    mentioned in the requirments file

    return : Libraries mentioned in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .") 
#-e fetches all the packages __init__ is present if we use pip install -r requirments.txt
# Here in setup.py file it is not required so we are removing as we have packages.

#Declaring variables for setup functions

PROJECT_NAME ="housing-predictor"
VERSION="0.0.7"
AUTHOR = "Rahul Mahajan"
DESCRIPTION = "Housing project deployment"
PACKAGES =["housing"] # not required after using find_packages
REQUIREMENTS_FILE_NAME="requirements.txt"



setup(


name = PROJECT_NAME,
version= VERSION,
author = AUTHOR,
description=DESCRIPTION,
packages = find_packages(),## Return all the folder name where we have __init__.py # Folder is package File is module Custom packags required
install_requires=get_requirements_list() # External packages required

)

if __name__ == "__main__":
    print(get_requirements_list())


"""
requirements.txt:

This helps you to set up your development environment.

Programs like pip can be used to install all packages listed in the file in one fell swoop. 
After that you can start developing your python script. Especially useful if you plan 
to have others contribute to the development or use virtual environments. 
This is how you use it


setup.py:

This helps you to create packages that you can redistribute.

The setup.py script is meant to install your package on the end user's system,
 not to prepare the development environment as pip install -r requirements.txt does. 
 
"""
