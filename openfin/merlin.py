import time
from pywinauto import Application
from pywinauto.keyboard import send_keys
from utils.logger import setup_logger
from utils.window_utils import wait_for_window

logger = setup_logger()

def open_merlin_screen(screen_id):
    logger.info(f"Opening Merlin screen: {screen_id}")
    dock_window = wait_for_window("Dock", timeout=60)

    if dock_window is None:
        logger.error("Dock window not found!")
        return False

    app = Application(backend='uia').connect(handle=dock_window.handle)
    dock_window = app.window(title="Dock")

    try:
        # Try identifying button by different attributes
        merlin_button = dock_window.child_window(title="Merlin", control_type="Button")

        if merlin_button.exists():
            merlin_button.click()
            logger.info("Clicked on Merlin button.")
        else:
            logger.error("Merlin button not found with title and control_type, trying with class_name.")
            merlin_button = dock_window.child_window(class_name="sc-c468fb75-0")  # Adjust class name if necessary
            
            if merlin_button.exists():
                merlin_button.click()
                logger.info("Clicked on Merlin button using class_name.")
            else:
                logger.info("Merlin button still not found! Attempting to navigate using keyboard.")
                for _ in range(8):  # Adjust tab count if necessary
                    send_keys("{TAB}")
                    time.sleep(0.5)
                send_keys("{ENTER}")
                logger.info("Pressed ENTER on selected element.")

    except Exception as e:
        logger.error(f"Error clicking Merlin button: {e}")
        return False

    screen_window = wait_for_window(screen_id, timeout=30)
    if screen_window is None:
        logger.error(f"Screen '{screen_id}' not found!")
        return False

    logger.info(f"{screen_id} screen opened successfully.")
    return True
