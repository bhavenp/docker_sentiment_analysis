import logging
from flask import Flask

from utils import initialize_logging
from ml_model_api import ml_model_bp

if __name__ == "__main__":

	initialize_logging("./logs/logging.yaml") # load and configure logging

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")
	
	app.register_blueprint(ml_model_bp)
	app.run(debug=True)
