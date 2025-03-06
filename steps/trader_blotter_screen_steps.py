from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Trader Blotter screen')
def step_impl(context):
    assert open_merlin_screen("trader-blotter")

@then('the Trader Blotter screen should be displayed')
def step_impl(context):
    # Verify the Trader Blotter screen is displayed logic can be added here
    pass