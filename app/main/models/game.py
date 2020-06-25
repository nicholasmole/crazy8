from time import sleep
from .deck import Deck
from .cards import Cards
from .writer import Writer
from .symbols import id_to_symbol, Symbols
from .player import Player
from ..services import play, write_out, events

class Game:
  """ Game Of Crazy 8"""

  def __init__(self, cards):
    self.deck = Deck(cards)
    self.turn = 0
    self.player_count = 4
    self.playing = True
    self.players = {}
    self.draw_limit = 0
    self.w = Writer(0.015)
    self.InputFailedAgain = 0

  def start_new_game(self):
    """ Start a New Game"""
    self.deck.Shuffle()
    self.add_players()
    self.deck.Discard(self.deck.Draw())

  def add_players(self):
    """ Add another Player To Game """
    for index in range(self.player_count):
      self.players[index] = Player(index, self.deck.draw_hand())

  def play_a_crazy_8(self) -> Cards:
    """ PLay"""
    print("")
    if self.is_computer_player():
      if self.get_player().has_cards():
        player = self.get_player()
        play.a_crazy_8(self.deck, Cards(player.hand[0].symbol,8))
      else:
        play.a_crazy_8(self.deck, Cards(Symbols.ANCHOR, 8))
      return True
     
    """ Human Player Picks a ccard """ 
    write_out.how_to_pick_suit(writer=self.w)
    self.user_plays_a_crazy_8()

  def expected_input(self, input, expected):
    return input in expected

  def user_plays_a_crazy_8(self):
    try:  
      picked_suit = input()
      if self.expected_input(picked_suit.lower(), ["a", "anchor"]):
        play.a_normal_card(Cards(Symbols.ANCHOR, 8), self.deck)
        return True
      elif self.expected_input(picked_suit.lower(), ["h", "heart"]):
        play.a_normal_card(Cards(Symbols.HEART, 8), self.deck)
        return True
      elif self.expected_input(picked_suit.lower(), ["c", "club"]):
        play.a_normal_card(Cards(Symbols.CLUB, 8), self.deck)
        return True
      elif self.expected_input(picked_suit.lower(), ["s", "star"]):
        play.a_normal_card(Cards(Symbols.STAR, 8), self.deck)
        return True
      return self.failed_play_8()
    except Exception as e:
      print(e)
      return self.failed_play_8()

  def failed_play_8(self):
    """ User Failed in attempt to play 8 card """
    self.w.write("Please select a suit to Continue")
    self.press_to_continue()
    return self.play_a_crazy_8()
  
  def get_player(self) -> Player:
    """ Get Current player"""
    return self.players[self.turn]
  
  def announce_played_card(self, card):
    """ When the player plays a card annouce it """
    if self.is_computer_player() is False:
      self.w.write("You played {} of {}".format(card.number, id_to_symbol(card.symbol)))

  def check_validate_card(self, card) -> bool:
    if card.number is 8:
      self.get_player().discard_card(card)
      play.a_normal_card(card, self.deck)
      self.play_a_crazy_8()
      self.announce_played_card(card)
      return True
    elif self.deck.matched_action_card(card=card):
      self.get_player().discard_card(card)
      play.a_normal_card(card, self.deck)
      if self.turn == 0:
        self.w.write("You played {} of {}".format(card.number, id_to_symbol(card.symbol)))
      return True
    return False

  def next_turn(self):
    self.turn += 1
    if self.turn > self.player_count - 1:
      self.turn = 0

  def draw_a_card(self, player = True):
    self.draw_limit += 1
    card = self.deck.Draw()
    print()
    if card is None:
      self.playing = False
      self.w.write("There are no more cards to draw")
      self.press_to_continue()
    else:
      if player:
        self.w.write("You drew a {} of {}".format(card.number, id_to_symbol(card.symbol)))
        self.press_to_continue()
      self.players[self.turn].hand.append(card)

  def get_counts(self):
    self.w.write("Card Count")
    index = 0
    for cards in self.players:
      self.w.write("Player {} has {} cards".format(index + 1, len(self.players[index].hand) ))
      index += 1
    sleep(0.5)
    self.press_to_continue()

  def press_to_continue(self):
    """ Press any key to continue """
    write_out.press_to_continue(self.w)
    self.check_if_quit()
    self.w.reset()

  def check_if_quit(self):
    """ Check if player is quitting """
    quit = input()
    if quit == "quit" or quit == "cancel": 
      self.playing = False

  def card_limit_reached(self):
    sleep(0.5)
    self.w.write("3 Cards Drawn")
    sleep(0.5)
    self.w.write("")
    self.w.write("Next Players Turn")
    self.w.write("")
    sleep(0.5)

  def computer_players_turn(self):
    """ Logic for Computer Players turn """
    if self.draw_limit >= 3:
      write_out.card_limit_reached(self.w)
      return
    if self.playing is False: 
      return
    found = False
    index = 0
    for cards in self.players[self.turn].hand:
      if cards.number == self.deck.action_card.number or cards.symbol == self.deck.action_card.symbol:
        found = True
        card = self.players[self.turn].hand[int(index)]
        if self.check_validate_card(card):
          write_out.computer_played(self.w, self.turn, card)
          self.press_to_continue()
          return True
      index += 1
    if found is False:
      self.w.write("Player {} Drew a card".format(self.turn + 1) )
      sleep(0.5)
      self.draw_a_card(player=False)
      self.computer_players_turn()

  def is_computer_player(self) -> bool:
    """ Determmine if computer player"""
    return self.turn > 0

  def restart_params_for_new_turn(self):
    """ Restarts Values when new turn starts """
    if self.is_computer_player() is False:
      self.w.clear()
    self.draw_limit = 0
    write_out.this_players_turn(self.w, self.turn)

  def Update(self):
    """ Another Turn Starts """
    self.restart_params_for_new_turn()

    if self.is_computer_player() is False:
      """ Human Player's turn """
      events.get_input(self)
    else:
      """ Computers Turn """
      write_out.top_card(self.w, self.deck.action_card)
      sleep(0.25)
      self.computer_players_turn()
    
    """ Check by Checking if this player has won"""
    self.has_this_player_won()
  
  def has_this_player_won(self):
    """ Has this player won """
    if self.playing:
      if self.players[self.turn].has_cards(): 
        self.next_turn()
        self.Update()
      else:
        write_out.this_player_wins(self.w, self.turn)
        