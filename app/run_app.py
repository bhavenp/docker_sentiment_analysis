import logging
from flask import Flask

from ml_model_api import ml_model_bp

if __name__ == "__main__":
    # logger.info("Initializing a Flask app...")

    app = Flask(__name__)
    app.register_blueprint(ml_model_bp)
    
    app.run(debug=True)
