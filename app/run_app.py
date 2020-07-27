import logging
from flask import Flask

from ml_model_api import ml_model_bp

if __name__ == "__main__":
	# start up a logger
	fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
	dateStr = "%m/%d/%Y %H:%M:%S"

	# output logs in same directory as this file
	LOGGING_FILE = "logs/app_logs.out"
	logging.basicConfig(filename=LOGGING_FILE,
	                    filemode='w',
	                    level=logging.DEBUG,
	                    format=fmtStr,
	                    datefmt=dateStr)

	app = Flask(__name__)
	app.logger.info("Initializing a Flask app...")
	
	app.register_blueprint(ml_model_bp)
	app.run(debug=True)
