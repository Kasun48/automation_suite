from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Dashboard screen')
def step_impl(context):
    if not context.result:  # Check if login was successful
        raise AssertionError("User must be logged in to open the Dashboard screen.")
    
    assert open_merlin_screen("Dashboard")

@then('the Dashboard screen should be displayed')
def step_impl(context):
    # Logic to verify if the Dashboard screen is displayed can be added here
    pass