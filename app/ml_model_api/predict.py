import os, sys

from model_training.pipelines import load_nn_model


# TODO: specify this path when starting up the app
MODEL_PATH = '../model_training/models/sentiment_dense_nn.keras'


def predict_online(data):
    """Predict from in-memory data on the fly.
    """
    try:
        
        nn_model = load_nn_model(MODEL_PATH)
        
        pred = nn_model.predict(data)
        pred = pred.tolist()
    except Exception as e:
        print(e)
        pred = []

    return pred
