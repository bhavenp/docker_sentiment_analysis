import os, sys, logging
from flask import Blueprint, current_app
from flask import request, jsonify
from flask import render_template


ui_bp = Blueprint('ui_bp', __name__) # create a Blueprint object


# create 'index' view
@ui_bp.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET": # user arrives at home page
        current_app.logger.info("Request made to home.")
        return render_template('index.html')

    elif request.method == "POST": # user inputted a sentence for prediction
        sentence = request.form['sentence']
        current_app.logger.info(f"User wants sentiment for '{sentence}'.")
        
        # pred = predict_online(model_path=current_app.model_path, data=[sentence]) # make the prediction for the sentence
        # pred_score = str(pred[0][0]) # pred is a list with another list inside of it
        pred_score = "1.0"
        current_app.logger.info(f"Sentiment score = {pred_score}")
        
        return render_template('after_prediction.html', sentence=sentence, pred_score=pred_score)
