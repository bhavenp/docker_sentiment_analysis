import os, sys
from pathlib import Path
import logging

from flask import Flask

from app.utils import initialize_logging
from app.ml_model_api import ml_model_bp

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

	@app.route("/hello")
	def hello():
		return "Hello World!"

	# Determine model_path based on location of this file
	app.model_path = dir_path.parents[0] / 'model_training/models/sentiment_dense_nn.keras'
	app.register_blueprint(ml_model_bp)

	return app


if __name__ == "__main__":
	create_app()