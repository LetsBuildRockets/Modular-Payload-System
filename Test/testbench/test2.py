# main.py
import os

import openhtf as htf
from openhtf.plugs.user_input import UserInput
from spintop_openhtf import TestPlan, TestSequence
from pprint import pprint
from time import sleep

#from static import SleepConfig

from openhtf.util import conf


FORM_LAYOUT = {
    'schema':{
        'title': "Test configuration",
        'type': "object",
        'required': ['operator', 'dutid', 'product'],
        'properties': {
            'operator': {
                'type': "string", 
                'title': "Enter the operator name"
            },
            'dutid': {
                'type': "string", 
                'title': "Enter the device under test serial number"
            },
            'product': {
                'type': "string", 
                'title': "Enter the product name"
            }
        }
    },
    'layout':[
        "operator", "dutid", "product",
    ]
}

""" Test Plan """

# This defines the name of the testbench.
plan = TestPlan('Sleep')

@plan.trigger('Configuration')
@plan.plug(prompts=UserInput)
def trigger(test, prompts):
    """Displays the configuration form"""
    response = prompts.prompt_form(FORM_LAYOUT)
    test.dut_id = response['dutid']
    test.state["operator"] = response['operator']
    test.state["product"] = response['product']
    if test.state["product"] == "A":
        test.state["run_sleep_2"] = True
    else:
        test.state["run_sleep_2"] = False
    pprint (response)

sequence = TestSequence('Sleep Sequence')

sequence = TestSequence('Sleep Sequence')
sub_seq = sequence.sub_sequence('Sleep Sub Sequence 1')
@sub_seq.testcase('Sleep Test 1A')
def sleep_test_1(test):
    """Waits five seconds"""
    test.attach('test_attachment', 'This is test attachment data.'.encode('utf-8'))
    test.attach_from_file( os.path.join(os.path.dirname(__file__), 'example_attachment.txt'))
    test_attachment = test.get_attachment('test_attachment')
    print(test_attachment)
    sleep(5)
    
@sub_seq.testcase('Sleep Test 1B')
def sleep_test_2(test):
    """Waits five seconds"""
    sleep(5)
    
sub_seq = sequence.sub_sequence('Sleep Sub Sequence 2')
@sub_seq.testcase('Sleep Test 2', run_if=lambda state: state.get('run_sleep_2', True))
def sleep_test_3(test):
    """Waits five seconds"""
    sleep(5)

plan.append(sequence)    

if __name__ == '__main__':
    plan.run_console()

    


