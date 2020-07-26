import logging
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds


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
