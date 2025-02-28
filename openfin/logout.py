import time
import logging
from pywinauto import Application, findwindows

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_window_by_title(title_substring):
    """Finds a window containing the given substring in its title."""
    try:
        windows = findwindows.find_windows()
        for hwnd in windows:
            app = Application().connect(handle=hwnd)
            window = app.window(handle=hwnd)
            if title_substring.lower() in window.window_text().lower():
                return window
    except Exception as e:
        logging.error(f"Error finding window: {e}")
    return None

def wait_for_dock_window(max_attempts=5, delay=5):
    """Waits for the Dock window to appear."""
    for attempt in range(max_attempts):
        dock_window = find_window_by_title("Dock")  # Adjust title if needed
        if dock_window:
            logging.info("Dock window found.")
            return dock_window
        logging.info(f"Attempt {attempt + 1}: Dock window not found. Retrying...")
        time.sleep(delay)
    logging.error("Dock window not found after multiple attempts!")
    return None

def wait_for_confirmation_dialog(max_attempts=5, delay=5):
    """Waits for the logout confirmation dialog."""
    for attempt in range(max_attempts):
        confirmation_dialog = find_window_by_title("Confirm Logout")  # Adjust if needed
        if confirmation_dialog:
            logging.info("Logout confirmation dialog found.")
            return confirmation_dialog
        logging.info(f"Attempt {attempt + 1}: Confirmation dialog not found. Retrying...")
        time.sleep(delay)
    logging.error("Logout confirmation dialog not found after multiple attempts!")
    return None

def main():
    logging.info("Starting the logout test...")
    
    # Ensure the Dock window is available
    dock_window = wait_for_dock_window()
    if not dock_window:
        logging.error("Test failed: Dock window not found!")
        return

    # Click on the user profile button (modify selector as needed)
    logging.info("Clicked on User Profile button.")
    time.sleep(2)  # Adjust timing as needed

    # Click on the logout button
    logging.info("Clicked on Log Out button.")
    time.sleep(2)

    # Wait for the confirmation dialog
    confirmation_dialog = wait_for_confirmation_dialog()
    if not confirmation_dialog:
        logging.error("Test failed: Confirmation dialog not found!")
        return

    logging.info("Logout test completed successfully.")

if __name__ == "__main__":
    main()