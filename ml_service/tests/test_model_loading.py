'''This file holds tests for loading a model.'''
from model_training.pipelines import load_nn_model

model_path = 'model_training/models/sentiment_dense_nn.keras'

def test_model_loading():
	model = load_nn_model(model_path)
	assert model # will be True if model is an object