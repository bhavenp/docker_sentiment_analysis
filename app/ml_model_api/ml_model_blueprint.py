import os, sys, logging
from flask import Blueprint, current_app
from flask import request, jsonify
from flask import render_template

from ml_model_api.predict import predict_online


ml_model_bp = Blueprint('ml_model_bp', __name__) # create a Blueprint object

# helper function so we can make predictions from home/ and predict/ endpoints
def make_prediction(sentences):
    return predict_online(data=sentences)

# create 'home' view for testing purposes
@ml_model_bp.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        current_app.logger.info("Request made to home.")
        return render_template('homepage/index.html')

    elif request.method == "POST":
        sentence = request.form['sentence']
        current_app.logger.info(f"User wants sentiment for '{sentence}'.")
        
        pred = make_prediction(sentences=[sentence]) # make the prediction for the sentence
        pred_score = str(pred[0][0]) # pred is a list with another list inside of it
        current_app.logger.info(f"Sentiment score = {pred_score}")
        
        return render_template('after_prediction/index.html', sentence=sentence, pred_score=pred_score)

# create route for prediction
@ml_model_bp.route("/predict", methods=["GET", "POST"])
def predict():
    """Performs an inference
    """
    if request.method == "POST":
        data = request.get_json()
        current_app.logger.debug(f"Input to \"predict\" endpoint: {data['sentences']}")
        pred = make_prediction(sentences=data["sentences"])
        current_app.logger.debug(f"Sentiment predictions = {pred}")
        
        return jsonify({"input": data, "pred": pred})

    if request.method == "GET":
        msg = "Please compose your request in POST type with data."
        current_app.logger.error(f"Wrong request type {request}.")
        return jsonify({"msg": msg})
