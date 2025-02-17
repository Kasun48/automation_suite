# openfin/login.py
import time
import pygetwindow as gw
from pywinauto import Application
from utils.config import USERNAME, PASSWORD, WINDOW_TITLE
from utils.logger import logger
from utils.window_utils import wait_for_window

def automate_login():
    logger.info("Waiting for the OpenFin login window to appear...")
    login_window = wait_for_window(WINDOW_TITLE)

    if login_window is None:
        logger.error("Login window not found!")
        return False

    app = Application(backend='uia').connect(handle=login_window._hWnd)
    dlg = app.window(title=WINDOW_TITLE)

    logger.info("Filling in login credentials...")
    username_field = dlg.child_window(control_type="Edit", found_index=0)
    password_field = dlg.child_window(control_type="Edit", found_index=1)
    login_button = dlg.child_window(title="Login", control_type="Button")

    username_field.set_text(USERNAME)
    password_field.set_text(PASSWORD)
    login_button.click()

    logger.info("Login attempt made.")
    time.sleep(5)  # Wait for login to process

    # Check for successful login (you may need to adjust this)
    # if "Dock" in [w.title for w in gw.getAllWindows()]:  # Adjust based on actual post-login title
    # Check for the window
    dock_window_title = "Dock"
    dock_window = wait_for_window(dock_window_title, timeout=30)

    if dock_window is not None:
        logger.info("Login successful.")
        return True
    else:
        logger.error("Login failed.")
        return False