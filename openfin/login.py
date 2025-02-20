# openfin/login.py
import time
import subprocess
from pywinauto import Application
from utils.config import USERNAME, PASSWORD, WINDOW_TITLE, BAT_FILE_PATH
from utils.logger import setup_logger
from utils.window_utils import wait_for_window, list_open_windows

logger = setup_logger()

def launch_application():
    logger.info("Launching OpenFin application...")
    subprocess.Popen(BAT_FILE_PATH)
    time.sleep(15)  # Adjust based on loading time

def automate_login():
    launch_application()
    
    logger.info("Waiting for the Mizuho login window to appear...")
    login_window = wait_for_window(WINDOW_TITLE)

    if login_window is None:
        logger.error("Login window not found! Current windows: %s", list_open_windows())
        return False

    app = Application(backend='uia').connect(handle=login_window._hWnd)
    dlg = app.window(title=WINDOW_TITLE)

    logger.info("Filling in login credentials...")
    username_field = dlg.child_window(control_type="Edit", title="username")
    password_field = dlg.child_window(control_type="Edit", title="password")
    auth_button = dlg.child_window(control_type="Button", title="Login")

    username_field.set_text(USERNAME)
    password_field.set_text(PASSWORD)
    auth_button.click()

    logger.info("Login attempt made.")
    time.sleep(10)  # Wait for the dock to load

    # Check for the dock window to confirm successful login
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is not None:
        logger.info("Login successful.")
        return True
    else:
        logger.error("Login failed. Current windows: %s", list_open_windows())
        return False