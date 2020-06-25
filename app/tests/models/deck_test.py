import unittest
from ...main.models.deck import Deck
from ...main.models.cards import Cards
from ...main.models.symbols import Symbols


class DeckTest(unittest.TestCase):
  
  def setup_deck(self) -> Deck:
    cards = []
    for symbol in range(1, 5):
      for number in range(1, 12):
        cards.append(Cards(symbol, number))
    return Deck(cards)

  def setUp(self):
    self.deck = self.setup_deck()

  def test_set_action_card(self):
    self.deck.set_action_card(Symbols.ANCHOR, 5)

    self.assertEqual(self.deck.action_card.symbol, Symbols.ANCHOR)

  def test_discard(self):
    self.deck.Discard(Cards(Symbols.ANCHOR, 5))

    self.assertEqual(self.deck.action_card.symbol, Symbols.ANCHOR)

  def test_draw_hand(self):
    hand = self.deck.draw_hand()

    self.assertEqual(len(hand), 7)
    
  def test_draw_a_card(self):
    card = self.deck.Draw()

    self.assertIsInstance(card, Cards)

    deck = self.setup_deck()
    deck.Shuffle()
    deck.pile = []
    deck.discard_pile = [Cards(Symbols.ANCHOR,5)]
    deck.Draw()
    deck.pile = []
    deck.discard_pile = []
    nocard = deck.Draw()

    self.assertIsNone(nocard)

  def test_matched_action_card(self):
    self.deck.action_card = Cards(Symbols.ANCHOR, 5)
    result = self.deck.matched_action_card(Cards(Symbols.ANCHOR, 4))

    self.assertEqual(result, True)
    

  def test_not_matched_action_card(self):
    self.deck.action_card = Cards(Symbols.HEART, 5)
    result = self.deck.matched_action_card(Cards(Symbols.ANCHOR, 4))

    self.assertEqual(result, False)

  def test_PlayDirectlyToDiscard(self):
    self.deck.pile[0] = Cards(Symbols.ANCHOR, 1)
    self.deck.PlayDirectlyToDiscard()
    result = self.deck.action_card.symbol

    self.assertEqual(result, Symbols.ANCHOR)

  def test_Shuffle(self):
    start = len(self.deck.pile)
    self.deck.Shuffle()
    result =len(self.deck.pile)

    self.assertEqual(start, result)

  def test_AddDiscardToPile(self):
    self.deck.PlayDirectlyToDiscard()
    self.deck.PlayDirectlyToDiscard()
    self.deck.PlayDirectlyToDiscard()
    start = len(self.deck.pile)
    self.deck.AddDiscardToPile()
    result = len(self.deck.pile)

    self.assertGreater(result, start)