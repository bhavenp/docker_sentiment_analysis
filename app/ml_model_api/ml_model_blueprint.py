import os, sys, logging
from flask import Blueprint
from flask import request, jsonify

from ml_model_api.predict import predict_online


# start up a logger
# fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
# dateStr = "%m/%d/%Y %H:%M:%S"

# # output logs in same directory as this file
# FILE_DIR = os.path.dirname(os.path.realpath(__file__)) 
# LOGGING_FILE = FILE_DIR + "/" + "app_logs.out"
# logging.basicConfig(filename=LOGGING_FILE,
#                     filemode='w',
#                     level=logging.DEBUG,
#                     format=fmtStr,
#                     datefmt=dateStr)
# logger = logging.getLogger("flask_app") # create a logger object

ml_model_bp = Blueprint('ml_model_bp', __name__) # create a Blueprint object

# create 'home' view for testing purposes
@ml_model_bp.route('/', methods=["GET", "POST"])
def home():
    # logger.info("Request made to home.")
    msg = "Flask app is up and running!"
    return jsonify({"msg": msg})

# create route for prediction
@ml_model_bp.route("/predict", methods=["GET", "POST"])
def predict():
    """Performs an inference
    """
    if request.method == "POST":
        data = request.get_json()
        # logger.debug(f"Input to predict/: {data}")
        pred = predict_online(data=data["sentences"])
        # pred = [-1] * len(data)
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        # logger.debug(f"Wrong request type {request}.")
        return jsonify({"msg": msg})