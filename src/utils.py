import logging
import sys


def init_logger():  # Create a logger named 'app'
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(created)f:%(levelname)s:%(name)s:%(module)s:%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
