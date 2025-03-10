from behave import when, then
from openfin.merlin import open_merlin_screen

@when('I open the Comments screen')
def step_impl(context):
    if not context.result:  # Check if login was successful
        raise AssertionError("User must be logged in to open the Comments screen.")
    
    assert open_merlin_screen("comments-main")

@then('the Comments screen should be displayed')
def step_impl(context):
    # Logic to verify if the Comments screen is displayed 
    pass