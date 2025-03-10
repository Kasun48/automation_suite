from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Settings screen')
def step_impl(context):
    assert open_merlin_screen("Settings")

@then('the Settings screen should be displayed')
def step_impl(context):
    # Verify the Settings screen is displayed logic can be added here
    pass