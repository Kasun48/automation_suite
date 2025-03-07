import time
from pywinauto import Desktop
from utils.logger import setup_logger

logger = setup_logger()

def wait_for_window(title, timeout=30):
    """Wait for a window with the specified title to appear."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        for window in Desktop(backend="uia").windows():
            if title in window.window_text():
                logger.info(f"Found window: {window.window_text()}")
                return window
        time.sleep(1)
    logger.error(f"Window '{title}' not found within {timeout} seconds.")
    return None

def list_open_windows():
    """List all open windows."""
    open_windows = []
    for window in Desktop(backend="uia").windows():
        open_windows.append(window.window_text())
    logger.info(f"Open windows: {open_windows}")
    return open_windows