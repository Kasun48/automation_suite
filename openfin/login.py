import time
import subprocess
import os
from pywinauto import Application
from utils.config import USERNAME, PASSWORD, WINDOW_TITLE, BAT_FILE_PATH
from utils.logger import setup_logger
from utils.window_utils import wait_for_window
from utils.screenshot import capture_screenshot
from openfin.logout import logout  # Import logout function

logger = setup_logger()

def launch_application():
    if not os.path.exists(BAT_FILE_PATH):
        logger.error(f"Batch file not found: {BAT_FILE_PATH}")
        capture_screenshot("bat_file_missing.png")
        raise FileNotFoundError(f"Batch file not found: {BAT_FILE_PATH}")

    logger.info("Launching OpenFin application...")
    subprocess.Popen(BAT_FILE_PATH)
    time.sleep(15)  # Adjust based on loading time

def automate_login(username=USERNAME, password=PASSWORD):
    try:
        launch_application()
    except FileNotFoundError:
        return False
    
    logger.info("Waiting for the Mizuho login window to appear...")
    login_window = wait_for_window(WINDOW_TITLE, timeout=60)

    if login_window is None:
        logger.error("Login window not found!")
        return False

    app = Application(backend='uia').connect(handle=login_window.handle)
    dlg = app.window(title=WINDOW_TITLE)

    logger.info("Filling in login credentials...")
    try:
        username_field = dlg.child_window(control_type="Edit", found_index=0)
        password_field = dlg.child_window(control_type="Edit", found_index=1)
        auth_button = dlg.child_window(control_type="Button", title="Login")

        username_field.set_text(username)
        password_field.set_text(password)
        auth_button.click()

        logger.info("Login attempt made.")
    except Exception as e:
        logger.error("Error during login: %s", e)
        return False

    time.sleep(10)  # Wait for the dock to load
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is not None:
        logger.info("Login successful.")
        logout()  # Call the logout function
        return True
    else:
        logger.error("Login failed.")
        return False

def validate_error_message(dlg):
    """Validate the error message displayed on the login screen."""
    try:
        error_field = dlg.child_window(control_type="Text", found_index=0)  # Adjust based on actual structure
        error_message = error_field.window_text()
        expected_message = "Login failed.\nIncorrect username and/or password OR Invalid/missing access token"
        if error_message == expected_message:
            logger.info("Error message validated successfully.")
            return True
        else:
            logger.error(f"Unexpected error message: {error_message}")
            return False
    except Exception as e:
        logger.error(f"Error validating error message: {e}")
        return False