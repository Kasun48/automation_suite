# tests/test_login.py
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openfin.launcher import launch_openfin
from openfin.login import automate_login
from utils.logger import logger

def test_login():
    launch_openfin()
    if automate_login():
        logger.info("Login test completed successfully.")
    else:
        logger.error("Login test failed.")

if __name__ == "__main__":
    test_login()