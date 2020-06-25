import unittest
from ...main.models.writer import Writer


class WriterTest(unittest.TestCase):

  def setUp(self):
    self.writer = Writer(0.0)
    
  def test_user(self):
    self.writer.reset()
    result = self.writer.speed
    self.assertEqual(result, 0.0)
