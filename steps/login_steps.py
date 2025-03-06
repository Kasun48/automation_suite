import logging
from behave import given, when, then
from openfin.login import automate_login, validate_error_message
from utils.screenshot import capture_screenshot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@given("the OpenFin application is launched")
def step_impl(context):
    logger.info("Launching the OpenFin application...")
    context.result = automate_login()
    logger.info("OpenFin application launched.")

@when("I enter valid credentials")
def step_impl(context):
    logger.info("Entering valid credentials...")
    context.result = automate_login(username=context.config.userdata['username'], password=context.config.userdata['password'])
    logger.info("Valid credentials entered.")

@when("I enter invalid credentials")
def step_impl(context):
    logger.info("Entering invalid credentials...")
    context.result = automate_login(username="invalid_user", password="wrong_password")
    logger.info("Invalid credentials entered.")

    # Validate the error message on the login screen
    login_window = wait_for_window("Mizuho Front Office", timeout=60)
    if login_window:
        app = Application(backend='uia').connect(handle=login_window.handle)
        dlg = app.window(title="Mizuho Front Office")
        if not validate_error_message(dlg):
            logger.error("Error message validation failed.")

@then("I should be logged in successfully")
def step_impl(context):
    if not context.result:
        screenshot_path = capture_screenshot("login_failure")
        logger.error(f"Login failed, check the screenshot: {screenshot_path}")
    assert context.result is True, "Login was not successful."

@then("I should see an error message")
def step_impl(context):
    if context.result:
        screenshot_path = capture_screenshot("invalid_login_success")
        logger.error(f"Invalid login was successful, check the screenshot: {screenshot_path}")
    assert context.result is False, "Error message not displayed for invalid login."