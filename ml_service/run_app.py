import os, sys
from pathlib import Path
import logging

from flask import Flask

from utils import initialize_logging
from ml_model_api import ml_model_bp
from model_training.pipelines import load_nn_model

'''
This is the application factory function.
Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.
'''
def create_app():

	dir_path = Path(os.path.dirname(os.path.realpath(__file__))) # get the path to the directory in which run_app.py resides
	logs_path = dir_path / "logs/logging.yaml"
	initialize_logging(logs_path, dir_path=dir_path) # load and configure logging

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")

	# Determine path to the model file based on location of this file
	model_path = dir_path / 'model_training/models/sentiment_dense_nn.keras'
	app.model = load_nn_model(model_path)
	app.register_blueprint(ml_model_bp)

	return app


if __name__ == "__main__":
	create_app()