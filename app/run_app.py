import logging
from flask import Flask

from app.utils import initialize_logging
from app.ml_model_api import ml_model_bp


def create_app():

	logs_path = "./logs/logging.yaml" #TODO: Determine logs/ path based on location of this file
	initialize_logging(logs_path) # load and configure logging

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")

	@app.route("/hello")
	def hello():
		return "Hello World!"

	#TODO: Determine model_path based on location of this file
	app.model_path = '../model_training/models/sentiment_dense_nn.keras'
	app.register_blueprint(ml_model_bp)

	return app


if __name__ == "__main__":
	create_app()