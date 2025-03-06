import logging
from behave import given, when, then
from openfin.login import automate_login, login_with_credentials, validate_error_message
from utils.screenshot import capture_screenshot
from utils.window_utils import wait_for_window
from pywinauto import Application

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
    login_with_credentials(context.dlg, context.config.userdata['username'], context.config.userdata['password'])
    logger.info("Valid credentials entered.")

@when("I enter invalid credentials")
def step_impl(context):
    logger.info("Entering invalid credentials...")
    login_window = wait_for_window("Mizuho Front Office", timeout=60)
    if login_window:
        context.dlg = Application(backend='uia').connect(handle=login_window.handle).window(title="Mizuho Front Office")
        login_with_credentials(context.dlg, "invalid_user", "wrong_password")
        logger.info("Invalid credentials entered.")
        
        # Validate the error message
        if not validate_error_message(context.dlg):
            logger.error("Error message validation failed.")

@then("I should be logged in successfully")
def step_impl(context):
    assert context.result is True, "Login was not successful."

@then("I should see an error message")
def step_impl(context):
    assert context.result is False, "Error message not displayed for invalid login."