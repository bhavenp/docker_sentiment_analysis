'''This file holds tests for loading a model and retrieving predictions to it.'''
from app.ml_model_api.predict import predict_online
from model_training.pipelines import load_nn_model

model_path = 'model_training/models/sentiment_dense_nn.keras'

def test_model_loading():
	model = load_nn_model(model_path)
	assert model # will be True if model is an object

def test_predict_online():
	sentence = ['Life is good!']
	prediction = predict_online(model_path, sentence)
	assert len(prediction) == 1