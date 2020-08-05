import logging
from flask import Flask

from utils import initialize_logging
from ml_model_api import ml_model_bp


def create_app():

	initialize_logging("./logs/logging.yaml") # load and configure logging

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")

	@app.route("/hello")
	def hello():
		return "Hello World!"

	app.model_path = '../model_training/models/sentiment_dense_nn.keras'
	app.register_blueprint(ml_model_bp)
	app.run(debug=True)

	return app


if __name__ == "__main__":
	create_app()