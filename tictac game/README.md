# Tic-Tac-Toe

A two-player Tic-Tac-Toe game with a desktop interface built with Python's
standard-library `tkinter` module.

## Run the game

From the repository root:

```bash
python "tictac game/main.py"
```

Players take turns by clicking an empty square. The game announces a winner
or a draw, and **New Game** resets the board.

## Run the tests

From the repository root:

```bash
pytest "tictac game/tests"
```

The tests cover the game rules without opening a graphical window.
