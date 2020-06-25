import random
from .cards import Cards

class Deck:
  """ List of cards
  """
  def __init__(self, cards = []):
    self.pile = cards
    self.discard_pile = []
    self.action_card = None

  def set_action_card(self, symbol, number):
    """ Set the Current Action Card"""
    self.action_card = Cards(symbol, number)

  def Discard(self, card):
    """ Add card to discard """
    self.action_card = card
    self.discard_pile.append(card)
  
  def draw_hand(self) -> list:
    hand = []
    for index in range(7):
      if len(self.pile) > 0:
        card = self.Draw()
        if card is not None:
          hand.append(card)
    return hand

  def Draw(self):
    """ Draw a card"""
    if len(self.pile) == 0:
      if len(self.discard_pile) > 0:
        self.AddDiscardToPile()
    if len(self.pile) == 0: 
      return None
    card = self.pile.pop(0)
    return card

  def matched_action_card(self, card) -> bool:
    """ Check if Action Card matches passed in Card """
    if card.symbol == self.action_card.symbol or card.number == self.action_card.number or card.number == 8:
      return True
    return False
  
  def PlayDirectlyToDiscard(self):
    """ Play card directly to Discard Pile"""
    self.Discard(card=self.Draw())
  
  def Shuffle(self):
    """ Shuffle cards in pile """
    self.pile = random.sample(self.pile, len(self.pile))
  
  def AddDiscardToPile(self):
    """ Move Discard to Pile"""
    self.pile.extend(self.discard_pile)
    self.discard_pile = []


    