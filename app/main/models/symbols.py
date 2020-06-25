class Symbols:
  """Symbols - distinct category of card
  """
  HEART   = 1
  CLUB    = 2
  ANCHOR  = 3
  STAR    = 4

def id_to_symbol(id) -> str:
  if id == Symbols.HEART:   return "Heart"
  if id == Symbols.CLUB:    return "Club"
  if id == Symbols.ANCHOR:  return "Anchor"
  if id == Symbols.STAR:    return "Star"
  return ""