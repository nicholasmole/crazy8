import unittest
from ...main.models.cards import Cards


class CardsTest(unittest.TestCase):
  def test_cards(self):
    card = Cards(1, 5)
    symbol = card.symbol
    number = card.number
    self.assertEqual(symbol, 1)
    self.assertEqual(number, 5)