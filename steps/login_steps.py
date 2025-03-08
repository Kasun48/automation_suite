import logging
from behave import given, when, then
from openfin.login import automate_login, login_with_credentials, validate_error_message
from utils.screenshot import capture_screenshot
from utils.window_utils import wait_for_window
from pywinauto import Application
from utils.config import USERNAME, PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@given("the OpenFin application is launched")
def step_impl(context):
    logger.info("Launching the OpenFin application...")
    context.dlg = automate_login()  # Save the dlg for later use
    logger.info("OpenFin application launched.")

@when("I enter valid credentials")
def step_impl(context):
    logger.info("Entering valid credentials...")
    if context.dlg is None:
        logger.error("Login dialog not found!")
        raise Exception("Login dialog not found!")
    login_with_credentials(context.dlg, USERNAME, PASSWORD)
    logger.info("Valid credentials entered.")

@when("I enter invalid credentials")
def step_impl(context):
    logger.info("Entering invalid credentials...")
    login_window = wait_for_window("Mizuho Front Office", timeout=60)

    if login_window:
        context.login_window = login_window
        context.dlg = Application(backend='uia').connect(handle=login_window.handle).window(title="Mizuho Front Office")
        login_with_credentials(context.dlg, INVALID_USERNAME, INVALID_PASSWORD)
        logger.info("Invalid credentials entered.")
        
        # Validate the error message
        if validate_error_message(context.dlg):
            logger.info("Error message validated successfully.")
        else:
            logger.error("Error message validation failed.")

@then("I should be logged in successfully")
def step_impl(context):
    dock_window = wait_for_window("Dock", timeout=60)
    if dock_window is None:
        logger.error("Dock window not found!")
        context.result = False
        assert False, "Dock window not faound! Login was not successful."

    try:
        app = Application(backend='uia').connect(handle=dock_window.handle)
        dock_window = app.window(title="Dock")
        if dock_window.exists():
            logger.info("Dock window detected. Login successful.")
            context.result = True
        else: 
            logger.error("Dock window not found after login!")
            context.result = False
            assert False, "Dock window not found after login!"
    except Exception as e:
        logger.error(f"Error connecting to Dock window: {e}")
        context.result = False
        assert False, f"Error connecting to Dock window: {e}"

    # Final assertion
    assert context.result, "Login was not succesfull."


@then("I should see an error message")
def step_impl(context):
    if not context.login_window:
        logger.info("Login dialog not found in context.")
        assert False, "Login dialog reference missing in context."

    # Validate the error message using the method from Login.py
    context.result = validate_error_message(context.dlg)

    # Assert that the error message was correctly displayed
    assert context.result, "Error message not displayed or incorrect."