from time import sleep
from ..models.symbols import id_to_symbol

def how_to_pick_suit(writer):
  """ How to Pick a Suit"""
  writer.write("Select New Suit: ")
  writer.write("a or Anchor")
  writer.write("h or Heart")
  writer.write("c or Club")
  writer.write("s or Star")

def top_card(writer, action_card):
  """The Current Top card"""
  writer.write("    > Current Card <")
  writer.write("|--                 --|")
  writer.write("      {} of {}     ".format(action_card.number, id_to_symbol(action_card.symbol)))
  writer.write("|--                 --|")
  writer.write(" ")

def players_hand(writer, player):
  index = 0
  writer.write("a)   Draw a card")
  writer.write("h)   See Hand Count")
  for cards in player.hand:
    writer.write("{})   {} of {}".format(index, cards.number, id_to_symbol(cards.symbol)))
    index+=1
  writer.write("<<<<<<<<<<<<<<<<")
  writer.write("Input Card To Use: ")
  writer.write(" ")

def this_player_wins(writer, turn):
  """ Write out that this person has won """
  writer.write("!!!!!!!!!!!!!!!!!!!!")
  writer.write("                    ")
  writer.write("Player {} Win!".format(turn))
  writer.write("                    ")
  writer.write("!!!!!!!!!!!!!!!!!!!!")

def this_players_turn(writer, turn):
  writer.reset()
  writer.write("<<<<<<<<<<<<<<<<")
  writer.write(" ")
  writer.write("Player {}'s turn".format(turn + 1))
  writer.write(" ")

def computer_played(writer, turn, card):
  sleep(0.5)
  writer.write("Player {} Played:".format(turn + 1))
  writer.write(" ")
  writer.write("    {} of {}".format(card.number, id_to_symbol(card.symbol)))

def press_to_continue(writer):
  writer.reset()
  writer.write(" ")
  writer.write("Press Enter to Continue ")
  writer.write(" ")

def card_limit_reached(writer):
  sleep(0.5)
  writer.write("3 Cards Drawn")
  sleep(0.5)
  writer.write("")
  writer.write("Next Players Turn")
  writer.write("")
  sleep(0.5)