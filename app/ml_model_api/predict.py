import os, sys

from pipelines import load_nn_model


# TODO: specify this path when starting up the app
MODEL_PATH = 'models/sentiment_dense_nn.keras'


def predict_online(data):
    """Predict from in-memory data on the fly.
    """
    try:
        
        nn_model = load_nn_model(MODEL_PATH)
        
        pred = nn_model.predict(data)
        pred = pred.tolist()
        # logger.info({"input": data, "pred": pred})
    except Exception as e:
        # logger.error(f"{e}")
        print(e)
        pred = []

    return pred
