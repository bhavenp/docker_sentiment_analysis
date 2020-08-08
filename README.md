# Dockerized Sentiment Analysis application

This repo is for developing a Dockerized sentiment analysis application that I built in [this repo](https://github.com/bhavenp/deployable_sentiment_analysis/).

## Steps
1. Build a Docker container that serves the sentiment analysis model. This model should only have to be loaded once when the containers starts up.
2. Build a Docker container that serves the UI through which users can submit a sentence. The UI will then send a request to the model container and show the related sentiment score.

## Present
1. You can run the backend part of the application by going into the `ml_app/` direcotry and following the instructions in the `README.md` file.

## Issues:
1. Pre-trainined model for embedding layer is cached locally, so when the cache is emptied automatically, tensorflow still thinks the model is cached locally.
	1. __Solution:__ I removed the directory where tensorflow_hub caches the model, then I reran the training process. Tested that the app works too.
