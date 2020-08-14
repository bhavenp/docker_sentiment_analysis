import os, sys, logging
from flask import Blueprint, current_app
from flask import request, jsonify

ml_model_bp = Blueprint('ml_model_bp', __name__) # create a Blueprint object


# create 'index' view for testing purposes
@ml_model_bp.route('/', methods=["GET", "POST"])
def index():
    return "ML model service is running!"

# helper method for predict/ endpoint
def get_pred(data):
    """Predict from in-memory data on the fly.
    """
    try:
        nn_model = current_app.model
        
        pred = nn_model.predict(data)
        pred = pred.tolist()
    except Exception as e:
        print(e)
        pred = []

    return pred

# create route for prediction
@ml_model_bp.route("/predict", methods=["GET", "POST"])
def predict():
    """Performs an inference
    """
    if request.method == "POST":
        data = request.get_json() # sentences come in through JSON
        current_app.logger.debug(f"Input to \"predict\" endpoint: {data['sentences']}")

        pred = get_pred( data=data["sentences"])
        current_app.logger.debug(f"Sentiment predictions = {pred}")
        
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        current_app.logger.error(f"Wrong request type {request}.")
        return jsonify({"msg": msg})
