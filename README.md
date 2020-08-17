# Dockerized Sentiment Analysis application

This repo is for developing a Dockerized sentiment analysis application that I built in [this repo](https://github.com/bhavenp/deployable_sentiment_analysis/). Most directories have a `README` file to describe what is going on and for me to take notes. Most of the code is commented so I can remember how things are working and learning lessons learned from this project.

## Development Steps
1. Build a Docker container that serves the sentiment analysis model as the _ml_service_. This model should only have to be loaded once when the container starts up.
2. Build a Docker container that serves the UI through which users can submit a sentence. This service is called the _ui_service_ The UI will then send a request to the model container and show the related sentiment score.
3. Use `docker-compose` to bring up both services and link them together.

## Steps to run Dockerized sentiment analysis application locally
1. From the root of this repo, run `docker-compose build` to build the images for the _ml_service_ and the _ui_service_. This will take a couple of minutes, especially since `tensorflow` is a large package.
	1. Run `docker images`. You should see images called `sentiment_analysis_ml_service` (for the _ml_service_) and `sentiment_analysis_ui_service` (for the _ui_service_).
2. Start up the _ml_service_ in the background by running `docker-compose up -d ml_service`.
	1. If you run `docker ps`, you should see a container running with the name `ml_service`.
	2. If you go to [http://localhost:8000/](http://localhost:8000/), you should see the message "ML model service is running!".
3. Start up the _ui_service_ by running `docker-compose up ui_service`.
	1. You should the logs for starting up the container for the _ui_service_ in your Terminal window.
	2. In a new Terminal window if you run `docker ps`, you should see a container running with the name `ui_service`.
	2. If you go to [http://localhost:8001/](http://localhost:8001/), you should see the web UI displayed.
4. Visit [http://localhost:8001/](http://localhost:8001/) and type in sentences that you would like to get the sentiment for!
5. Clean-up:
	1. Run `docker rm -f ui_service ml_service` to stop and remove the containers.
	2. Run `docker ps -a` to verify that there are no containers running.

### Alternative
1. Run `docker-compose up` from the root of the repo. This will build images for both services and start them up. The logs for both services will print to your Terminal window.
2. Go to [http://localhost:8001/](http://localhost:8001/) to use the application.

