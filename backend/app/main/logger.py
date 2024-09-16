import json
import logging
from logging.config import dictConfig

from main import settings


def get_logger(name: str = "app"):
    config_dir = f"{settings.BASE_DIR.parent}/config"

    with open(f"{config_dir}/logger.json", "r") as f:
        logging_config = json.load(f)

    logging.config.dictConfig(config=logging_config)
    return logging.getLogger(name=name)
