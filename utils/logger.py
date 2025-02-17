# utils/logger.py
import logging

def setup_logger():
    logger = logging.getLogger("OpenFinAutomation")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("automation.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()