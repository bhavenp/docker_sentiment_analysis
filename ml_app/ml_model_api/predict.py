import os, sys

from model_training.pipelines import load_nn_model


def predict_online(model_path, data):
    """Predict from in-memory data on the fly.
    """
    try:
        
        nn_model = load_nn_model(model_path)
        
        pred = nn_model.predict(data)
        pred = pred.tolist()
    except Exception as e:
        print(e)
        pred = []

    return pred
