# main.py
from openhtf.plugs.user_input import UserInput
from spintop_openhtf import TestPlan

""" Test Plan """

# This defines the name of the testbench.
plan = TestPlan('hello')

@plan.testcase('Hello-Test')
@plan.plug(prompts=UserInput)
def hello_world(test, prompts):
    prompts.prompt('Hello Operator!')
    test.dut_id = 'hello' # Manually set the DUT Id to same value every test

if __name__ == '__main__':
    plan.no_trigger()
    plan.run_console()