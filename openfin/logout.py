import time
from pywinauto import Application, Desktop, keyboard
from utils.logger import setup_logger
from utils.window_utils import wait_for_window
import os
import sys

logger = setup_logger()

def wait_for_confirmation_dialog(timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        for window in Desktop(backend="uia").windows():
            if "Confirmation" in window.window_text():
                logger.info(f"Found Confirmation Dialog: {window.window_text()}")
                return window
        time.sleep(1)
    return None

def click_confirm_button(confirmation_dlg, retries=5):
    for attempt in range(retries):
        logger.info(f"Attempt {attempt + 1} to click Confirm button.")
        confirm_button = confirmation_dlg.child_window(aria_label="Confirm", control_type="Button")
        
        if confirm_button.exists() and confirm_button.is_enabled():
            confirm_button.click()
            logger.info("Logout confirmed.")
            return True
        
        time.sleep(1)

    logger.info("Confirm button not found or not enabled after retries, trying keyboard input.")
    try:
        confirmation_dlg.set_focus()
        time.sleep(1)

        logger.info("Pressing TAB key twice to reach Confirm Button...")
        send_keys("{TAB}")
        time.sleep(0.5)
        send_keys("{TAB}")
        time.sleep(0.5)
        send_keys("{ENTER}")
        logger.info("Logout confirmed via keyboard input.")
        return True
    except Exception as e:
        logger.error("Error during keyboard input for confirmation: %s", e)
        return False

def logout():
    logger.info("Logging out of the application...")
    dock_window = wait_for_window("Dock", timeout=60)
    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window.handle)
    dock_window = app.window(title="Dock")

    try:
        user_profile_button = dock_window.child_window(title="User Profile", control_type="Button")
        user_profile_button.click()
        logger.info("Clicked on User Profile button.")
    except Exception as e:
        logger.error("Error clicking User Profile button: %s", e)
        return False

    user_profile_window = wait_for_window("User Profile", timeout=30)
    if user_profile_window is None:
        logger.error("User Profile window not found!")
        return False

    user_profile_app = Application(backend='uia').connect(handle=user_profile_window.handle)
    user_profile_window = user_profile_app.window(title="User Profile")

    try:
        log_out_button = user_profile_window.child_window(title="Log Out", control_type="Button")
        log_out_button.click()
        logger.info("Clicked on Log Out button.")
    except Exception as e:
        logger.error("Error clicking Log Out button: %s", e)
        return False

    try:
        time.sleep(5)

        logger.info("Pressing TAB key twice to reach Confirm Button...")
        keyboard.send_keys("{TAB}")
        time.sleep(0.5)
        keyboard.send_keys("{TAB}")
        time.sleep(0.5)
        keyboard.send_keys("{ENTER}")
        logger.info("Logout confirmed via keyboard input.")
        return True
    except Exception as e:
        logger.error("Error during keyboard input for confirmation: %s", e)
        return False

    logger.info("Logging out completed. Terminating application.")
    os._exit(0)  # Terminate the script after logout