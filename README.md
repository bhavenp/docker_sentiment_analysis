# Deployable Sentiment Analysis model

This repo is for developing a sentiment analysis model that can be deployed using a Flask application. 
This project is an extension of the [ComputeFest 2020- "Notebook to Cloud" workshop](https://github.com/Harvard-IACS/2020-ComputeFest).

## Steps
1. Build a training pipeline to train & save a sentiment analysis model.
2. Build a Flask app that has an endpoint that can receive data in the form of sentences and return sentiment predictions/scores.
3. Build a GUI through which users can submit a sentence. GUI will then show the sentiment score.

## Present
1. Use the the `sentiment_analysis_env.yaml` file at the root of the repo to create a Conda environment and start it.
	1. Run `conda env create -f sentiment_analysis_env.yaml`.
	2. Run `conda activate sentiment_analysis_env` to start the Conda environment.
2. Install the project by running `pip install -e .`. This will allow all of the modules to be imported correctly.
3. Change directory to the `app/` directory and run `python run_app.py` to start up the app. There are two ways to interact with the application:
	1. The app will start up on [http://127.0.0.1:5000/](http://127.0.0.1:5000/), which is the home page. A user can input a sentence in the provided text box and click _Submit_ to get a sentiment score for the given sentence.
	2. The app also accomodates HTTP POST requests, which can be sent to [http://127.0.0.1:5000/predict/](http://127.0.0.1:5000/predict/) to get sentiment scores for multiple sentences.
		1. The body of the POST request should look like:
		```
		{
			"sentences":[
						  "this place is the worst!",
            			  "this place is the best!",
            			  "I love this place."
            			]
        }
		```
		2. This can be done using an application such as [Postman](https://www.postman.com/).

## Future work
1. There will be a single Docker container that will serve as an endpoint. Prediction will be served from this endpoint.
2. I want to add a container that controls a GUI.
3. I want to add a container that runs a SQL database that will store previous queries to the model and the results.

