from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Sales Blotter screen')
def step_impl(context):
    assert open_merlin_screen("Sales Blotter")

@then('the Sales Blotter screen should be displayed')
def step_impl(context):
    # Verify the Sales Blotter screen is displayed logic can be added here
    pass