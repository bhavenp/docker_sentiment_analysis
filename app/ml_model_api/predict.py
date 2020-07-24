import logging
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))); # so I can load utils

from pipelines.train_model import load_keras_hub_model

# logger = logging.getLogger(__name__)

# TODO: specify this path when starting up the app
MODEL_PATH = 'pipelines/models/sentiment_dense_nn.keras'
# logger.info(f"Path to model: {MODEL_PATH}")

def predict_online(data):
    """Predict from in-memory data on the fly.
    """
    print(f"Predicting for {data}")
    try:
        print(os.getcwd())
        
        checkpoint = load_keras_hub_model(MODEL_PATH)
        print("Successfully loaded the model")
        pred = checkpoint.predict(data)
        pred = pred.tolist()
        # logger.info({"input": data, "pred": pred})
    except Exception as e:
        # logger.error(f"{e}")
        print(e)
        pred = []

    return pred
