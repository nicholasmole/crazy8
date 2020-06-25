import unittest
from ...main.models.player import Player
from ...main.models.cards import Cards


class PlayerTest(unittest.TestCase):

  def setUp(self):
    self.player = Player(1, [Cards(1, 1)])

  def test_has_card(self):
    result = self.player.has_cards()
    self.assertEqual(result, True)