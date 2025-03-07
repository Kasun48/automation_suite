from behave import given, when, then
from openfin.logout import logout
from utils.screenshot import capture_screenshot  # Updated import
from utils.logger import setup_logger

logger = setup_logger()

@given("I am logged in to the application")
def step_impl(context):
    context.result = True  # Assume already logged in for this step

@when("I log out")
def step_impl(context):
    context.result = logout()

@then("I should be logged out successfully")
def step_impl(context):
    if not context.result:
        capture_screenshot("logout_failure.png")  # Updated to use capture_screenshot
        logger.error("Logout failed, check the screenshot.")
    assert context.result is True, "Logout was not successful."