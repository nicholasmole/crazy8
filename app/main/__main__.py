from .models.cards import Cards
from .models.symbols import Symbols
from .models.game import Game


cards = []
for symbol in range(1, 5):
  for number in range(1, 12):
    cards.append(Cards(symbol, number))



def main():
  game = Game(cards)
  game.start_new_game()
  game.Update()


if __name__ == '__main__':
  main()