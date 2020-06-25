import builtins  # The module which contains the call to input
import sys
import unittest
import time
from ...main.services.delay_print import delay_print


class DelayTest(unittest.TestCase):

  def setUp(self):
    builtins.print = lambda start='', end='': ''
    sys.stdout.write = lambda x: ''
    time.sleep = lambda x: ''
    
  def test_user(self):
    self.assertIsNone(delay_print("testthis",  0.0))
