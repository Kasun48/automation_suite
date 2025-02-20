# openfin/logout.py
import time
from pywinauto import Application
from utils.logger import setup_logger
from utils.window_utils import wait_for_window, list_open_windows

logger = setup_logger()

def logout():
    logger.info("Logging out of the application...")

    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window._hWnd)
    dock_window = app.window(title="Dock")

    # Click on the Layout Settings button
    layout_settings_button = dock_window.child_window(title="Layout Settings", control_type="Button")
    layout_settings_button.click()

    # Wait for the menu items to appear
    time.sleep(2)

    # Click on the "Quit" menu item
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