import time
import pyautogui

def capture_screenshot(name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    pyautogui.screenshot(filename)
    return filename