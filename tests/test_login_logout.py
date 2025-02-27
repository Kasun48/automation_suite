# tests/test_login_logout.py
from openfin.login import automate_login
from openfin.logout import logout
from utils.logger import setup_logger

logger = setup_logger()

def test_login_logout():
    logger.info("Starting the login/logout test...")
    
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