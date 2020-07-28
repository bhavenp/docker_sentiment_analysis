import sys,logging
from pathlib import Path
from utils import load_yaml

def initialize_logging(config_path):
    """Initialize logger from path.
    """
    try:
        config = load_yaml(config_path)
        logging.config.dictConfig(config)
    except Exception as e:
        # if fail
        logging.basicConfig(level=logging.INFO,
                            filename="./logs/info.log",
                            filemode='w')
        logging.info(f"{e}. Falling back to default logger.")

    finally:
        logging.info(f"Logging initialized.")