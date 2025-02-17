# utils/window_utils.py
import pygetwindow as gw
import time

def wait_for_window(title, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        windows = gw.getWindowsWithTitle(title)
        if windows:
            return windows[0]
    return None