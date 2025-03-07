from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Historical Trader Blotter screen')
def step_impl(context):
    assert open_merlin_screen("historical-trader-blotter")

@then('the Historical Trader Blotter screen should be displayed')
def step_impl(context):
    # Verify the Historical Trader Blotter screen is displayed logic can be added here
    pass