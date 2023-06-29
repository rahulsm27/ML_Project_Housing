from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(error_message=e,error_detail=sys)
        logging.info(housing.error_message)
    logging.info("we are testing logging module")

    return "Starting Machine Learning project"

if __name__ == "__main__":
    app.run(debug=True) 