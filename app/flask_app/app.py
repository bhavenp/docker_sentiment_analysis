# import logging

from flask import Flask, request, jsonify

from predict import predict_online
# from ml_deploy_demo.util.utils import initialize_logging

# logger = logging.getLogger(__name__)
# initialize_logging(config_path='/app/logging.yaml')

app = Flask(__name__)

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
        # logger.debug(f"Input to predict/: {data}")
        pred = "Making prediction" #predict_online(data=data["data"])
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        # logger.debug(f"Wrong request type {request}.")
        return jsonify({"msg": msg})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
