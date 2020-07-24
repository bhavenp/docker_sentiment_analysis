import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))); # so I can load utils

import re
from pathlib import Path
import logging
#import joblib

import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

from utils import load_yaml


# This example is taken from:
# https://www.tensorflow.org/tutorials/keras/text_classification_with_hub
def run_training_pipeline(config_model, logger):
    """ runs pipeline to train keras Dense NN model for sentiment classification """

    # Split the training set into 60% and 40%, so we'll end up with 15,000 examples
    # for training, 10,000 examples for validation and 25,000 examples for testing.
    train_data, validation_data, test_data = tfds.load(
        name="imdb_reviews", 
        split=('train[:60%]', 'train[60%:]', 'test'),
        as_supervised=True)

    # Word Embeddings from Tensorflow-Hub
    embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
    hub_layer = hub.KerasLayer(embedding, input_shape=[],
                               dtype=tf.string, trainable=True)

    # Model
    print("Creating model")
    model = tf.keras.Sequential()
    model.add(hub_layer)
    for _ in range(config_model['params']['hidden_layers']):
        model.add(tf.keras.layers.Dense(
            config_model['params']['hidden_units'],
            activation='relu'))
    # add output layer
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    # Compilation
    model.compile(optimizer='adam', 
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=['accuracy'])

    # Train
    history = model.fit(train_data.shuffle(10000).batch(512),
                    epochs=config_model['params']['num_epochs'],
                    validation_data=validation_data.batch(512),
                    verbose=1)
    # Test
    results = model.evaluate(test_data.batch(512), verbose=2);

    for name, value in zip(model.metrics_names, results):
        logger.info("%s: %.3f" % (name, value))
        print("%s: %.3f" % (name, value));

    # Save model
    model_name = config_model["name"]
    save_path = os.path.join("./models", f"{model_name}.keras")
    model.save(save_path)
    logger.info("Saved keras pipeline model at {0}".format(save_path))

    # Load & Check Consistency
    checkpoint = load_keras_hub_model(save_path)
    check_data = test_data.batch(512)
    assert np.all(
        checkpoint.predict(check_data) == model.predict(check_data)
    )
    logger.info("Keras saved model passed consistency check")

def load_keras_hub_model(save_path):
    return tf.keras.models.load_model(save_path,
        custom_objects={'KerasLayer': hub.KerasLayer}
    )

if __name__ == "__main__":
    # get configurations for model
    DEFAULT_SETTINGS = "default_settings.yml"
    config = load_yaml(DEFAULT_SETTINGS)
    config_model = config['model']

    # start up a logger
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
    dateStr = "%m/%d/%Y %H:%M:%S"
    logging.basicConfig(filename=config['logging']['config_path'],
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)
    logger = logging.getLogger("training_model") # create a logger object
    print("Loaded configuration settings.")
    logger.info("Model name: {0}".format(config_model['name']))
    logger.info("Model params: hidden_units={0}, hidden_layers={1}, num_epochs={2}".format(
        config_model['params']["hidden_units"], 
        config_model['params']["hidden_layers"], 
        config_model['params']["num_epochs"]) )


    run_training_pipeline(config_model, logger)
