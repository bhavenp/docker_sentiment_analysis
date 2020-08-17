import os, sys
from pathlib import Path
import logging

from flask import Flask

from utils import initialize_logging
from ui_api import ui_bp

'''
This is the application factory function.
Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.
'''
def create_app(ml_service_url="http://0.0.0.0:8000/predict"):

	dir_path = Path(os.path.dirname(os.path.realpath(__file__))) # get the path to the directory in which run_app.py resides
	logs_path = dir_path / "logs/logging.yaml"
	initialize_logging(logs_path, dir_path=dir_path) # load and configure logging

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")

	@app.route("/hello")
	def hello():
		return "Hello World!"

	app.ml_service_url = ml_service_url # Bind the URL to connect to the ml-service for predictions
	app.register_blueprint(ui_bp)

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(port=8001, debug=True)