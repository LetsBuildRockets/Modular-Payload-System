#from unittest import TestCase
import openhtf as htf
from openhtf.plugs.user_input import UserInput
from spintop_openhtf import TestPlan
from spintop_openhtf import PhaseResult

#from openhtf.output.callbacks import console_summary
from outputs import ConsoleSummary

from psu_plug import PSU

""" Test Plan """

# This defines the name of the testbench.
plan = TestPlan('PSU')

@plan.testcase('Hello-Test')
@plan.plug(prompts=UserInput)
def hello_world(test, prompts):
    #prompts.prompt('Hello Operator!')
    test.dut_id = 'hello' # Manually set the DUT Id to same value every test

@plan.testcase('setup')
@plan.plug(psu=PSU)
def psuu(test, psu):
    try:
        test.logger.info(f"Connected to Supply: {psu.psu.identify()}")
    except Exception as error:
        test.logger.error("failed to connect to supply")
        test.logger.error(error)
        return PhaseResult.STOP

REQ_123_crit = htf.Measurement('vout').doc("VOUT").in_range(4.5,5.5)
@plan.testcase('REQ_123')
@plan.plug(psu=PSU)
@htf.measures(REQ_123_crit)
def criteria_test(test, psu):
    value_ = psu.psu.getVoltage(1)
    test.measurements.vout = value_


@plan.teardown('cleanup')
@plan.plug(prompts=UserInput)
def cleanup(test, prompts):
    """clean up..."""
    #prompts.prompt('exit?')
    test.logger.info('Cleaned up.')


if __name__ == '__main__':
    plan.no_trigger()    
    plan.add_callbacks(ConsoleSummary())
    #plan.add_callbacks(ConsoleMeasurements())
    plan.run_once()