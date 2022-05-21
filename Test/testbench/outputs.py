"""Module to display test summary on console."""

import os
import sys

from openhtf.core import measurements
from openhtf.core import test_record
import six


class ConsoleSummary():
  """Print test results with failure info on console."""

  # pylint: disable=invalid-name
  def __init__(self, verbose=False, indent=2, output_stream=sys.stdout):
    self.indent = ' ' * indent
    if os.name == 'posix' or True:  # Linux and Mac.
      self.RED = '\033[91m'
      self.GREEN = '\033[92m'
      self.ORANGE = '\033[93m'
      self.RESET = '\033[0m'
      self.BOLD = '\033[1m'
    else:
      self.RED = ''
      self.GREEN = ''
      self.ORANGE = ''
      self.RESET = ''
      self.BOLD = ''

    self.color_table = {
        test_record.Outcome.PASS: self.GREEN,
        test_record.Outcome.FAIL: self.RED,
        test_record.Outcome.ERROR: self.ORANGE,
        test_record.Outcome.TIMEOUT: self.ORANGE,
        test_record.Outcome.ABORTED: self.RED,
    }

    self.verbose = verbose
    self.output_stream = output_stream

  # pylint: enable=invalid-name

  def __call__(self, record):
    output_lines = [
        ''.join((self.color_table[record.outcome], self.BOLD,
                 record.code_info.name, ':', record.outcome.name, self.RESET))
    ]
    if record.outcome != test_record.Outcome.PASS or self.verbose:
      for phase in record.phases:
        new_phase = True
        phase_time_sec = (float(phase.end_time_millis) -
                          float(phase.start_time_millis)) / 1000.0
        for name, measurement in six.iteritems(phase.measurements):
          if measurement.outcome != measurements.Outcome.PASS or self.verbose:
            if new_phase:
              output_lines.append('phase: %s [ran for %.2f sec]' %
                                  (phase.name, phase_time_sec))
              new_phase = False

            output_lines.append('%sitem: %s (%s)' %
                                (self.indent, name, measurement.outcome))
            output_lines.append('%smeasured_value: %s' %
                                (self.indent * 2, measurement.measured_value))
            output_lines.append('%svalidators:' % (self.indent * 2))
            for validator in measurement.validators:
              output_lines.append('%svalidator: %s' %
                                  (self.indent * 3, str(validator)))

        phase_result = phase.result.phase_result
        if not phase_result:  # Timeout.
          output_lines.append('timeout phase: %s [ran for %.2f sec]' %
                              (phase.name, phase_time_sec))
        elif 'CONTINUE' not in str(phase_result):  # Exception.
          output_lines.append('%sexception type: %s' %
                              (self.indent, record.outcome_details[0].code))

    output_lines.append('\n')
    text = '\n'.join(output_lines)
    self.output_stream.write(text)