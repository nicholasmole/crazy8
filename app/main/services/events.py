from . import write_out

def get_input(game):
  if game.draw_limit >= 3:
    write_out.card_limit_reached(game.w)
    return
  if game.playing == False:
    return False
  try:
    game.w.write(" ")
    write_out.top_card(game.w, game.deck.action_card)
    write_out.players_hand(game.w, game.players[0])
    picked = input()
    if picked == "quit" or picked == "cancel": 
      game.playing = False
      return False
    if picked == "a": 
      game.draw_a_card()
      return get_input(game)
    if picked == "h": 
      game.get_counts()
      return get_input(game)
    card = game.players[0].hand[int(picked)]
    if game.check_validate_card(card):
      return True
    else:
      game.w.write("This card can not be played")
      game.press_to_continue()
      return get_input(game)
  except Exception as e:
    print(e)
    return input_failed(game)

def input_failed(game):
  if game.InputFailedAgain is 0:
    game.w.write("Please provide a number corresponding to your hand")
    game.press_to_continue()
    if game.playing is False: 
      return False
    game.InputFailedAgain += 1
  return get_input(game)