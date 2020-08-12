import logging
import yaml


def load_yaml(yaml_path):
	try:
		with open(yaml_path, "r") as f:
			config = yaml.safe_load(f)
	except Exception as e:
		logging.error("Failed to load a {0} due to {1}".format(yaml_path, e))
	return config