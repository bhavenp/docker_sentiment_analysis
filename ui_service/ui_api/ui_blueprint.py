import os, sys, logging
from flask import Blueprint, current_app
from flask import request as flask_request
from flask import jsonify
from flask import render_template
import requests


ui_bp = Blueprint('ui_bp', __name__) # create a Blueprint object


def send_prediction_request(sentence):
    try:
        response = requests.post('http://0.0.0.0:8000/predict', 
            json={"sentences": [sentence]})
    except requests.exceptions.ConnectionError: # Catch error when ML service is not running
        return "Could not connect to \'http://0.0.0:8000/predict\'. Check if the ML service is running."
    except Exception as e: # Catch all other errors
        return str(e)

    if response.status_code != 200:
        return "Error in sending request to ML model endpoint"
    
    json_data = response.json()
    return str(json_data['pred'][0][0]) # pred is a list with another list inside of it


# create 'index' view
@ui_bp.route('/', methods=["GET", "POST"])
def home():
    if flask_request.method == "GET": # user arrives at home page
        current_app.logger.info("Request made to home.")
        return render_template('index.html')

    elif flask_request.method == "POST": # user inputted a sentence for prediction
        sentence = flask_request.form['sentence']
        current_app.logger.info(f"User wants sentiment for '{sentence}'.")
        
        # pred = predict_online(model_path=current_app.model_path, data=[sentence]) # make the prediction for the sentence
        # pred_score = str(pred[0][0]) 
        pred_score = send_prediction_request(sentence)
        current_app.logger.info(f"Sentiment score = {pred_score}")
        
        return render_template('after_prediction.html', sentence=sentence, pred_score=pred_score)
