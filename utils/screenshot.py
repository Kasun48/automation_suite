from PIL import ImageGrab
import os

def take_screenshot(filename):
    """Take a screenshot and save it to the specified filename."""
    screenshot = ImageGrab.grab()
    screenshot.save(os.path.join('reports', filename))
    print(f"Screenshot saved as {filename}")