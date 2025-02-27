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
    login_window = wait_for_window(WINDOW_TITLE, timeout=60)

    if login_window is None:
        logger.error("Login window not found! Current windows: %s", list_open_windows())
        return False

    app = Application(backend='uia').connect(handle=login_window._hWnd)
    dlg = app.window(title=WINDOW_TITLE)

    logger.info("Available controls in the window: %s", dlg.print_control_identifiers())

    logger.info("Filling in login credentials...")
    try:
        username_field = dlg.child_window(control_type="Edit", found_index=0)  # Adjusting to use index
        password_field = dlg.child_window(control_type="Edit", found_index=1)  # Adjusting to use index
        auth_button = dlg.child_window(control_type="Button", title="Login")

        username_field.set_text(USERNAME)
        password_field.set_text(PASSWORD)
        auth_button.click()

        logger.info("Login attempt made.")
    except Exception as e:
        logger.error("Error during login: %s", e)
        return False

    time.sleep(10)  # Wait for the dock to load
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is not None:
        logger.info("Login successful.")
        return True
    else:
        logger.error("Login failed. Current windows: %s", list_open_windows())
        return False