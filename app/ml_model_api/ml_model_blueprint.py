import os, sys, logging
from flask import Blueprint, current_app
from flask import request, jsonify

from ml_model_api.predict import predict_online


ml_model_bp = Blueprint('ml_model_bp', __name__) # create a Blueprint object

# create 'home' view for testing purposes
@ml_model_bp.route('/', methods=["GET", "POST"])
def home():
    current_app.logger.info("Request made to home.")
    msg = "Flask app is up and running!"
    return jsonify({"msg": msg})

# create route for prediction
@ml_model_bp.route("/predict", methods=["GET", "POST"])
def predict():
    """Performs an inference
    """
    if request.method == "POST":
        data = request.get_json()
        current_app.logger.debug(f"Input to \"predict\" endpoint: {data['sentences']}")
        pred = predict_online(data=data["sentences"])
        current_app.logger.debug(f"Sentiment predictions = {pred}")
        
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        current_app.logger.error(f"Wrong request type {request}.")
        return jsonify({"msg": msg})