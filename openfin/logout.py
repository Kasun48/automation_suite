# openfin/logout.py
import time
from pywinauto import Application
from utils.logger import setup_logger
from utils.window_utils import wait_for_window, list_open_windows

logger = setup_logger()

def logout():
    logger.info("Logging out of the application...")

    # Wait for the Dock window to appear
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window._hWnd)
    dock_window = app.window(title="Dock")

    # Click on the User Profile button in the Dock
    try:
        user_profile_button = dock_window.child_window(title="User Profile", control_type="ActionButton")
        user_profile_button.click()
        logger.info("Clicked on User Profile button.")
    except Exception as e:
        logger.error("Error clicking User Profile button: %s", e)
        return False

    # Wait for the User Profile window to appear
    user_profile_window = wait_for_window("User Profile", timeout=30)

    if user_profile_window is None:
        logger.error("User Profile window not found!")
        return False

    user_profile_app = Application(backend='uia').connect(handle=user_profile_window._hWnd)
    user_profile_window = user_profile_app.window(title="User Profile")

    # Click the Log Out button
    try:
        log_out_button = user_profile_window.child_window(title="Log Out", control_type="Button")
        log_out_button.click()
        logger.info("Clicked on Log Out button.")
    except Exception as e:
        logger.error("Error clicking Log Out button: %s", e)
        return False

    # Wait for the confirmation dialog to appear
    confirmation_dialog = wait_for_window("Log Out of [UAT] Front Office Apps - v19.2.12", timeout=30)

    if confirmation_dialog is None:
        logger.error("Confirmation dialog not found!")
        return False

    confirmation_app = Application(backend='uia').connect(handle=confirmation_dialog._hWnd)
    confirmation_dlg = confirmation_app.window(title="Log Out of [UAT] Front Office Apps - v19.2.12")

    # Click the Confirm button to log out
    try:
        confirm_button = confirmation_dlg.child_window(aria_label="Confirm", control_type="Button")
        confirm_button.click()
        logger.info("Logout confirmed.")
    except Exception as e:
        logger.error("Error during logout confirmation: %s", e)
        return False

    return True