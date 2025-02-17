# tests/test_login.py
from openfin.launcher import launch_openfin
from openfin.login import automate_login
from openfin.logout import logout
from utils.logger import logger

def test_login_logout():
    launch_openfin()
    if automate_login():
        logger.info("Login test completed successfully.")
        if logout():
            logger.info("Logout test completed successfully.")
        else:
            logger.error("Logout test failed.")
    else:
        logger.error("Login test failed.")

if __name__ == "__main__":
    test_login_logout()