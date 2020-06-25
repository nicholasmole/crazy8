"""Play a card
"""
def a_crazy_8(deck, card8):
  deck.set_action_card(card8.symbol, card8.number)

def a_normal_card(card, deck):
  """ Deck Plays this card"""
  deck.Discard(card)

