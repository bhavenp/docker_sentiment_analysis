import sys
import logging
import numpy as np

from utils import load_yaml


if __name__ == "__main__":
    # get configurations for model
    if sys.argv.ge

    config = load_yaml(DEFAULT_SETTINGS)
    config_model = config['model']

    # # start up a logger
    # fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Message: %(message)s"
    # dateStr = "%m/%d/%Y %H:%M:%S"
    # logging.basicConfig(filename=config['logging']['config_path'],
    #                     level=logging.DEBUG,
    #                     format=fmtStr,
    #                     datefmt=dateStr)
    # logger = logging.getLogger("training_model") # create a logger object
    # print("Loaded configuration settings.")
    # logger.info("Model name: {0}".format(config_model['name']))
    # logger.info("Model params: hidden_units={0}, hidden_layers={1}, num_epochs={2}".format(
    #     config_model['params']["hidden_units"], 
    #     config_model['params']["hidden_layers"], 
    #     config_model['params']["num_epochs"]) )


    # run_training_pipeline(config_model, logger)
