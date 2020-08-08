## Start-up Flask application running the model
1. Run `python run_app.py` to start up the Flask application. This will default to "debug" mode for the application.
	1. Currently, the app will only use the `models/sentiment_dense_nn.keras` model, since this is hard-coded in `ml_model_api/predict.py`. A future version of this app should allow the user to specify which model to load.


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
