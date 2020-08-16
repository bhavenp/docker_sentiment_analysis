This directory contains the code for the frontend service of the application, which is referred to as the _ui-service_. This service displays a nice UI in a web browser for the user to interact with. Users are able to type out their sentences and get sentiment predictions for their sentences.

## Start-up the UI service WITH DOCKER
1. Run `docker build <docker_repo_name>/<tag> .` to build the Docker image. The `Dockerfile` contains the instructions for building the Docker image.
2. Run `docker images` to find the Docker image ID for the image you just built.
3. Run `docker run -d -p 8001:8001 --name=sentiment-anlysis-frontend <docker_image_ID> <ml-service_URL>`.
	1. The _ui-service_ will start up in the background on [http://0.0.0.0:8001/](http://0.0.0.0:8001/), so you should see UI when you visit that page.
	2. The `ml-service_URL` is an _optional_ parameter that can be specified. If not specified, the _ui-service_ will try to connect with the _ml-service_ at 'http://0.0.0:8000/predict'.
	2. __IMPORTANT:__ If the `ml-service_URL` is a `localhost` address then the _ml-service_ will not be available to the _ui-service_, even if the _ml-service_ is running locally or in a Docker container. You will get an error message that says the UI could not connect to the _ml-service_ because the _localhost_ inside of a Docker container is not the same _localhost_ as your computer. You must use `docker-compose` to bring up both services together and couple them.
4. Stop the container using `docker stop <container_ID>` and remove it using `docker rm <container_ID>`.

## Start-up the UI service WITHOUT DOCKER
1. Use the the `sentiment_analysis_ui_env.yaml` file in this directory to create a Conda environment and start it.
	1. Run `conda env create -f sentiment_analysis_ui_env.yaml`.
	2. Run `conda activate sentiment_analysis_ui_env` to start the Conda environment.
2. Install the project by running `pip install -e .`. This will allow all of the modules for this part of the application to be imported correctly.
3. Test that this backend application can be run properly using `pytest`.
	1. Run `pytest -v` from this directory. This will test the application using the tests contained in the `tests/` directory.
	2. At the bottom of your Terminal screen, you should see `3 passed`, indicating that the app should work correctly.
4. Start up the application locally:
	1. From the root directory, execute `chmod +x run.sh`. This shell script will start up a Gunicorn server that runs the Flask application.
	2. From the root directory, execute `./run.sh`. An optional second argument can be provided to specify the URL for the _ml-service_ by running `./run.sh <ml-service_URL>`.
		1. If a no arguments are provided, then the _ui-service_ will assume the _ml-service_ is running on `http://0.0.0.0:8000`.
	3. The app will start up on [http://0.0.0.0:8001/](http://0.0.0.0:8001/), which is the home page. A user can input a sentence in the provided text box and click _Submit_ to get a sentiment score for the given sentence.
	4. __IMPORTANT:__ A sentiment score will only be returned if the ML service is running (in a Docker container or just locally). If the ML service is not running, you should see a message that says "Could not connect to 'http://0.0.0:8000/predict'." or the specified URL to the _ml-service_.


## Folder Descriptions
1. `logs`: Contains different _.log_ files that provide information on how a user interacted with the application and any errors that occurred.
	1. The `logging.yaml` file specifies configurations for the logger used by the Flask application.

2. `static`: Contains the CSS and JavaScript code for the GUI component of the application.
3. `templates`: Contains the Jinja templates that are served as part of the GUI.
	1. `base.html` is the base template that `index.html` and `after_prediction.html` build off of.
	2. The HTML, CSS and JavaScript code was adapted from the _Eventually_ design by [HTML5 UP](html5up.net).
4. `tests/`: Contains test files for testing the frontend application.
5. `ui_api`: Contains files implementing the frontend API of the service.
	1. `ui_blueprint.py` contains a Flask Blueprint that details which endpoints are served and how they are served.
6. `utils`: Contains code and functions that can be shared.
	1. `initialize_logging.py`: Starts up the logger with the proper configurations.
	2. `load_yaml`: Reads in the configuration details from a YAML file.
