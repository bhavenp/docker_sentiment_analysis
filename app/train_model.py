import sys
import logging
import numpy as np

from utils import load_yaml


if __name__ == "__main__":
    # get configurations for model
    if len(sys.argv) == 1:
        print("Please provide path to a model configuration file.")
        sys.exit(2) # exit code of 2 means there was a command-line error
    else:
        model_config_file = sys.argv[1]

    config_map = load_yaml(model_config_file)
    model_config_params = config_map['model']


    # start up a logger
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
    dateStr = "%m/%d/%Y %H:%M:%S"
    logging.basicConfig(filename=config_map['logging']['output_file_path'],
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)
    logger = logging.getLogger("training_model") # create a logger object
    print("Loaded configuration settings.")
    logger.info("Model name: {0}".format(model_config_params['name']))
    logger.info("Model params: hidden_units={0}, hidden_layers={1}, num_epochs={2}".format(
        model_config_params['params']["hidden_units"], 
        model_config_params['params']["hidden_layers"], 
        model_config_params['params']["num_epochs"]) )


    # run_training_pipeline(config_model, logger)
