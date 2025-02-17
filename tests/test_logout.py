# tests/test_logout.py
from openfin.logout import logout
from utils.logger import logger

def test_logout():
    logout()
    logger.info("Logout test completed.")

if __name__ == "__main__":
    test_logout()