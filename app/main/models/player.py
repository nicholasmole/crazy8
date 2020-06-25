class Player:
  """ Game Player
  """
  def __init__(self, id, hand = []):
    self.id = id
    self.hand = hand

  def has_cards(self) -> bool:
    return len(self.hand) > 0
  
  def discard_card(self, card):
    """ Remove Card From Hand """
    index = 0
    for playable in self.hand:
      if playable.number == card.number and playable.symbol == card.symbol:
        break
      index += 1

    del self.hand[index]
