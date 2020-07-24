import os, sys, logging
from flask import Flask, request, jsonify

from predict import predict_online


# start up a logger
fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
dateStr = "%m/%d/%Y %H:%M:%S"

# output logs in same directory as this file
FILE_DIR = os.path.dirname(os.path.realpath(__file__)) 
LOGGING_FILE = FILE_DIR + "/" + "app_logs.out"
logging.basicConfig(filename=LOGGING_FILE,
                    filemode='w',
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)
logger = logging.getLogger("flask_app") # create a logger object

app = Flask(__name__) # create app object

# create route for 'homepage' for testing purposes
@app.route('/', methods=["GET", "POST"])
def home():
    logger.info("Request made to home.")
    msg = "Flask app is up and running!"
    return jsonify({"msg": msg})

# create route for prediction
@app.route("/predict", methods=["GET", "POST"])
def predict():
    """Performs an inference
    """
    if request.method == "POST":
        data = request.get_json()
        logger.debug(f"Input to predict/: {data}")
        pred = predict_online(data=data["sentences"])
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        logger.debug(f"Wrong request type {request}.")
        return jsonify({"msg": msg})

if __name__ == '__main__':
    port = 5000
    logger.info("Opened port {0} .".format(port))

    app.run(port=port, debug=True)
