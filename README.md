# Deployable Sentiment Analysis model

This repo is for developing a sentiment analysis model that can be deployed using a Flask application. 
This project is an extension of the [ComputeFest 2020- "Notebook to Cloud" workshop](https://github.com/Harvard-IACS/2020-ComputeFest).

## Steps
1. Build a training pipeline to train & save a sentiment analysis model.
2. Build a Flask app that has an endpoint that can receive data in the form of sentences and return sentiment predictions/scores.
3. Build a GUI through which users can submit a sentence. GUI will then show the sentiment score.

## Future work
1. There will be a single Docker container that will serve as an endpoint. Prediction will be served from this endpoint.
2. I want to add a container that controls a GUI.
3. I want to add a container that runs a SQL database that will store previous queries to the model and the results.

