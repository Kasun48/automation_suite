import time
from pywinauto import Application
from utils.logger import setup_logger
from utils.window_utils import wait_for_window

logger = setup_logger()

def open_merlin_screen(screen_id):
    logger.info(f"Opening Merlin screen: {screen_id}")
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window._hWnd)
    dock_window = app.window(title="Dock")

    try:
        merlin_button = dock_window.child_window(title="Merlin", control_type="Button")
        merlin_button.click()
        logger.info("Clicked on Merlin button.")
    except Exception as e:
        logger.error("Error clicking Merlin button: %s", e)
        return False

    screen_window = wait_for_window(screen_id, timeout=30)
    if screen_window is None:
        logger.error(f"Screen '{screen_id}' not found!")
        return False

    logger.info(f"{screen_id} screen opened successfully.")
    return True