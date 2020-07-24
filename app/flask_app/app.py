import logging

from flask import Flask, request, jsonify

# from predict import predict_online


# start up a logger
fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
dateStr = "%m/%d/%Y %H:%M:%S"
logging.basicConfig(filename="app_logs.out",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)
logger = logging.getLogger("flask_app") # create a logger object

app = Flask(__name__) # create app object

@app.route('/', methods=["GET", "POST"])
def home():
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
        pred = "Making prediction" #predict_online(data=data["data"])
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        logger.debug(f"Wrong request type {request}.")
        return jsonify({"msg": msg})

if __name__ == '__main__':
    port = 5000
    logger.info("Opened port {0} .".format(port))

    app.run(port=port, debug=True)
