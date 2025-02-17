# openfin/logout.py
import time
import pygetwindow as gw
from pywinauto import Application
from utils.logger import logger
from utils.window_utils import wait_for_window

def logout():
    logger.info("Logging out of the application...")

    # Wait for the dock window to appear
    dock_window_title = "Dock"  # Adjust this title
    dock_window = wait_for_window(dock_window_title)

    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window._hWnd)
    dock_window = app.window(title=dock_window_title)

    # Click on the menu button to open the logout options
    menu_button = dock_window.child_window(control_type="Button", found_index=1)  # Adjust based on the actual control
    menu_button.click()

    # Wait for the menu to expand and show items
    time.sleep(2)

    # Click on the "Quit" option
    quit_option = dock_window.child_window(title="Quit[DEV] Front Office Apps - v19.2.12", control_type="MenuItem")
    quit_option.click()

    # Wait for the confirmation dialog to appear
    confirmation_window = wait_for_window("Confirmation", timeout=30)

    if confirmation_window is None:
        logger.error("Confirmation dialog not found!")
        return False

    confirmation_app = Application(backend='uia').connect(handle=confirmation_window._hWnd)
    confirmation_dlg = confirmation_app.window(title="Confirmation")

    # Click the Confirm button to log out
    confirm_button = confirmation_dlg.child_window(aria_label="Confirm", control_type="Button")
    confirm_button.click()

    logger.info("Logout confirmed.")
    return True