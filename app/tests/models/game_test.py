import builtins  # The module which contains the call to input
import sys
import unittest
import time
from ...main.models.game import Game
from ...main.models.deck import Deck
from ...main.models.cards import Cards
from ...main.models.symbols import Symbols
from ...main.models.writer import Writer



class GameTest(unittest.TestCase):

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

  def test_start_new_game(self):
    self.game.start_new_game()

    self.assertIsNotNone(self.game.deck.action_card)

  def test_play_game(self):
    self.game.start_new_game()
    self.game.deck.action_card = Cards(Symbols.ANCHOR, 1)
    self.game.players[0].hand[0] = Cards(Symbols.ANCHOR, 2)
    self.game.Update()

    self.assertIsNotNone(self.game.deck.action_card)

  def test_check_if_player_won(self):
    self.game.start_new_game()
    self.game.has_this_player_won()

    self.assertEqual(self.game.playing, False)

  def test_play_cards(self):
    self.game.start_new_game()
    self.game.turn = 0
    self.game.players[0].hand = [Cards(Symbols.ANCHOR, 3)]
    self.game.check_validate_card(card=Cards(Symbols.ANCHOR, 3))

    self.assertEqual(self.game.playing, True)

  def test_computer_play_cards(self):
    time.sleep = lambda x: ''
    self.game.start_new_game()
    self.game.deck.action_card = Cards(Symbols.ANCHOR, 1)
    self.game.turn = 1
    self.game.players[1].hand = [Cards(Symbols.ANCHOR, 3)]
    self.game.computer_players_turn()

    self.assertEqual(self.game.playing, False)

    self.game.start_new_game()
    self.game.deck.action_card = Cards(Symbols.ANCHOR, 1)
    self.game.turn = 1
    self.game.players[1].hand = [Cards(Symbols.STAR, 3)]
    self.game.computer_players_turn()

    self.assertEqual(self.game.playing, False)

  def test_card_limit_reached(self):
    self.game.start_new_game()
    self.game.card_limit_reached()
    self.game.next_turn()
    
    self.assertEqual(self.game.playing, True)

  def test_get_counts(self):
    self.game.start_new_game()
    self.game.get_counts()
    self.game.announce_played_card(card = Cards(Symbols.ANCHOR, 1))
    
    self.assertEqual(self.game.playing, False)

  def test_play_a_crazy_8(self):
    self.game.start_new_game()
    self.game.turn = 1
    self.game.players[1].hand = []
    self.game.play_a_crazy_8()
    
    self.assertEqual(self.game.playing, True)

  def test_user_plays_a_crazy_8(self):
    self.game.start_new_game()
    for value in ['a','h','c','s']:
      self.game.turn = 0
      self.game.players[0].hand = []
      builtins.input = lambda: value
      self.game.user_plays_a_crazy_8()
    builtins.input = lambda: 'quit'
    
    self.assertEqual(self.game.playing, True)

  def test_draw_a_card(self):
    self.game.start_new_game()
    self.game.draw_a_card()
    
    self.assertGreater(len(self.game.players[0].hand), 6)

  def tearDown(self):
    builtins.input = input
    builtins.print = print
    sys.stdout.write = sys.stdout.write
    Writer.clear = Writer.clear
    time.sleep = time.sleep