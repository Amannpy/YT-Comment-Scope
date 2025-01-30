import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger; can be used across modules."""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    # Ensure the logs directory exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger