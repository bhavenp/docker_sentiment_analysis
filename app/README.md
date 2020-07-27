## Train a model
1. Run `train_model.py <path_to_model_configuration_file>`.
	1. The `model_configuration_file` should be a YAML file containing all the parameters as seen in `training_configs/settings_v1.yml`.
	2. The trained model should be saved in the `models/` directory.

## Start-up Flask application running the model
1. Run `python run_app.py` to start up the Flask application. This will default to "debug" mode for the application.
	1. Currently, the app will only use the `models/sentiment_dense_nn.keras` model, since this is hard-coded in `ml_model_api/predict.py`. A future version of this app should allow the user to specify which model to load. 
