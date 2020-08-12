This directory contains the code for the frontend of the application, which displays a nice UI in a web browser for the user to interact with. Users are able to type out their sentences and get sentiment predictions for their sentences.

## Start-up the Flask application running the UI WITHOUT DOCKER
1. Use the the `sentiment_analysis_ui_env.yaml` file in this directory to create a Conda environment and start it.
	1. Run `conda env create -f sentiment_analysis_ui_env.yaml`.
	2. Run `conda activate sentiment_analysis_ui_env` to start the Conda environment.
2. Install the project by running `pip install -e .`. This will allow all of the modules for this part of the application to be imported correctly.
3. Test that this backend application can be run properly using `pytest`.
	1. Run `pytest -v` from this directory. This will test the application using the tests contained in the `tests/` directory.
	2. At the bottom of your Terminal screen, you should see `3 passed`, indicating that the app should work correctly.
4. Start up the application locally:
	1. From the root directory, execute `chmod +x run.sh`. This shell script will start up a Gunicorn server that runs the Flask application.
	2. From the root directory, execute `./run.sh`.
	3. The app will start up on [http://0.0.0.0:8001/](http://0.0.0.0:8001/), which is the home page. A user can input a sentence in the provided text box and click _Submit_ to get a sentiment score for the given sentence.


## Folder Descriptions
1. `logs`: Contains different _.log_ files that provide information on how a user interacted with the application and any errors that occurred.
	1. The `logging.yaml` file specifies configurations for the logger used by the Flask application.
2. `ml_model_api`: Contains files implementing the backend of the application.
	1. `ml_model_blueprint.py` contains a Flask Blueprint that details which endpoints are served and how they are served.
	2. `predict.py` contains a single function, `predict_online`, that loads the `models/sentiment_dense_nn.keras` model and uses the loaded model to predict sentiment scores for the user-inputted sentences.
3. `static`: Contains the CSS and JavaScript code for the GUI component of the application.
4. `templates`: Contains the Jinja templates that are served as part of the GUI.
	1. `base.html` is the base template that `index.html` and `after_prediction.html` build off of.
	2. The HTML, CSS and JavaScript code was adapted from the _Eventually_ design by [HTML5 UP](html5up.net).
5. `utils`: Contains code and functions that are shared. Currently, it only contains a single Python file called `initialize_logging.py`, which starts up the logger with the proper configurations.
