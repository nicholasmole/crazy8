import builtins  # The module which contains the call to input
import sys
import unittest
import time
from ...main.models.game import Game
from ...main.models.deck import Deck
from ...main.models.cards import Cards
from ...main.models.symbols import Symbols
from ...main.models.writer import Writer
from ...main.models.player import Player
from ...main.services.events import get_input, input_failed

class EventsTest(unittest.TestCase):

  def setUp(self):
    cards = []
    for symbol in range(1, 5):
      for number in range(1, 12):
        cards.append(Cards(symbol, number))

    self.game = Game(cards)
    builtins.input = lambda: 'quit'
    builtins.print = lambda start='', end='': ''
    sys.stdout.write = lambda x: ''
    Writer.clear = lambda x: ''
    time.sleep = lambda x: ''

  def test_events(self):

    result = get_input(self.game)
    self.assertEqual(result, False)

    self.game.draw_a_card = 3
    result = get_input(self.game)
    self.assertEqual(result, False)
    
    self.game.draw_a_card = 0
    builtins.input = lambda: 'a'
    result = get_input(self.game)
    self.assertEqual(result, False)

    self.game.players[0] = Player(0,[Cards(Symbols.ANCHOR, 1)])
    self.game.deck.action_card = Cards(Symbols.ANCHOR, 1)
    
    builtins.input = lambda: '0'
    result = get_input(self.game)
    self.assertEqual(result, False)

  def test_input_failed(self):
    builtins.input = lambda: 'quit'
    result = input_failed(self.game)
    self.assertEqual(result, False)

    self.game.playing = True
    self.game.InputFailedAgain = 0
    result = input_failed(self.game)
    self.assertEqual(result, False)
    

  def tearDown(self):
    builtins.input = input
    builtins.print = print
    sys.stdout.write = sys.stdout.write
    Writer.clear = Writer.clear
    time.sleep = time.sleep