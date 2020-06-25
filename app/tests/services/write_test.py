import builtins  # The module which contains the call to input
import sys
import time
import unittest
from ...main.models.writer import Writer
from ...main.models.cards import Cards
from ...main.models.player import Player
from ...main.services.write_out import *


class WriterTest(unittest.TestCase):

  def setUp(self):
    self.writer = Writer(0.0)
    self.player = Player(0, [Cards(1,1)])
    builtins.input = lambda: 'quit'
    builtins.print = lambda start='', end='': ''
    sys.stdout.write = lambda x: ''
    Writer.clear = lambda x: ''
    time.sleep = lambda x: ''
    
  def test_writeout(self):
    how_to_pick_suit(self.writer)
    self.assertEqual(self.writer.speed, 0.0)

    top_card(self.writer, Cards(1, 1))
    self.assertEqual(self.writer.speed, 0.0)

    players_hand(self.writer, self.player)
    self.assertEqual(self.writer.speed, 0.0)
    
    this_player_wins(self.writer, 0)
    self.assertEqual(self.writer.speed, 0.0)

    computer_played(self.writer, 0, Cards(1,1))
    self.assertEqual(self.writer.speed, 0.0)

    press_to_continue(self.writer)
    self.assertEqual(self.writer.speed, 0.0)

    card_limit_reached(self.writer)
    self.assertEqual(self.writer.speed, 0.0)



  def tearDown(self):
    builtins.input = input
    builtins.print = print
    sys.stdout.write = sys.stdout.write
    Writer.clear = Writer.clear
    time.sleep = time.sleep