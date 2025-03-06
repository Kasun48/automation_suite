from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Position Manager screen')
def step_impl(context):
    assert open_merlin_screen("position-manager")

@then('the Position Manager screen should be displayed')
def step_impl(context):
    # Verify the Position Manager screen is displayed logic can be added here
    pass