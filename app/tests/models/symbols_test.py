import unittest
from ...main.models.symbols import Symbols, id_to_symbol


class SymbolsTest(unittest.TestCase):

  def test_symbols_is(self):
    result = id_to_symbol(Symbols.HEART)
    self.assertEqual(result, "Heart")

    result = id_to_symbol(Symbols.CLUB)
    self.assertEqual(result, "Club")

    result = id_to_symbol(Symbols.ANCHOR)
    self.assertEqual(result, "Anchor")

    result = id_to_symbol(Symbols.STAR)
    self.assertEqual(result, "Star")

    result = id_to_symbol("")
    self.assertEqual(result, "")