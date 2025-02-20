# utils/window_utils.py
import time
import pygetwindow as gw

def wait_for_window(title, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        windows = gw.getWindowsWithTitle(title)
        if windows:
            return windows[0]
    return None

def list_open_windows():
    return [w.title for w in gw.getAllWindows()]