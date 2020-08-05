import sys,logging
from pathlib import Path
from model_training.utils import load_yaml

def initialize_logging(config_path, dir_path=None):
    """Initialize logger from path.
    """
    try:
        config = load_yaml(config_path)
        
    except Exception as e:
        # if fail
        logging.basicConfig(level=logging.INFO,
                            filename="./logs/info.log",
                            filemode='w')
        logging.info(f"{e}. Falling back to default logger.")
    else:
        if dir_path is not None: # Update path to log files using provided directory path
            for handler_name in config['handlers']:
                handler = config['handlers'][handler_name]
                if 'filename' in handler.keys():
                    filename = Path(handler['filename'])
                    handler['filename'] = dir_path / filename

        logging.config.dictConfig(config)

    finally:
        logging.info(f"Logging initialized.")