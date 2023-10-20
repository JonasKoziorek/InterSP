from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import the names of callback functions you want to test
from controller import display, update

# Normal unit test
def test_update_callback():
    output = update(1, 0)
    assert output == 'button 1: 1 & button 2: 0'

# UITest
def test_display_callback():
    ctx = copy_context()
    def run_callback():
        for key, value in ctx.keys, ctx.values: 
            print(key)
            print(value)
        context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "btn-1-ctx-example.n_clicks"}]}))
        return display(1, 0, 0, ctx)
    output = ctx.run(run_callback)
    assert output == f'You last clicked button with ID btn-1-ctx-example'