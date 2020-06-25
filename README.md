# Crazy8

Create a terminal playable game of crazy8s

To start a game run `make game` or `python3 run.py`


## Requirements

This game was developed to require no external library requirements to play

This game was built in Python 3.7 with the exact version number below. 

`Python 3.7.4 (default, Sep  7 2019, 18:27:02)`

For testing the application does require the installation of `unittest` and `coverage`.

Use the following method to run tests

`python3 -m unittest app/tests/*/**.py`

## Playing the Game

In its current interation the crazy8 game always has 4 players and always has a deck of 4 suits with 11 cards each.

To start a game run `make game` or `python3 run.py`

You may run "quit" to exit the game at anytime.

The user will be prompted with several options. Simple type in the character
corresponding to the action you would like to take.


```
a - draw a new card (Limit 3 per turn)
h - Show number of cards each player has remaing
0 - Card you can play
....
n + 1 - All other cards that you 

```

The rule of crazy 8's is you must match  the "Current Card" either by suit
or by number.

If you can not match the "Current Card" by suit or number you must draw a card.

When drawing cards the house rule limits you to 3 draws. If you draw the 
third card you instantly lose your turn and the next player goes.

If you have an "8" or "crazy 8" you can play that card whenever you please

When played you will be prompted to select a new suit

```
Select New Suit: 
a or Anchor
h or Heart
c or Club
s or Star
```

After selecting the new suit the card "Current Card" will reflect this
new suit.

After your turn the computer Players will take their turns. They will play
a card, draw a card, or play a crazy 8.

The game continues until the first player has reached 0 cards in their hand.


## Getting with Python and Pip start

All of these commands should be run from **python 3**
Start by sourcing the virtual enviroment

```
    source venv/bin/activate
```

If you virtual enviroment does not exist run this command using python

```
    python -m venv venv
```


Installing libraries from requirements

```
    python -m pip install -r requirements.txt
```

Remember to update packages requirements with

```
    pip freeze > requirements.txt
```

Run tests

`python3 -m unittest app/tests/*/**.py`

Then Check coverage

```
    coverage run -m unittest app/tests/*.py && coverage report 
```
