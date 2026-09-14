"""Tests for the Tic-Tac-Toe game rules."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from logic import TicTacToe


def play(game: TicTacToe, moves: list[tuple[int, int]]) -> None:
    for move in moves:
        assert game.make_move(*move)


def test_new_game_starts_with_empty_board_and_x_turn() -> None:
    game = TicTacToe()

    assert game.board == [["", "", ""], ["", "", ""], ["", "", ""]]
    assert game.current_player == "X"
    assert not game.game_over


def test_players_alternate_after_valid_moves() -> None:
    game = TicTacToe()

    assert game.make_move(0, 0)
    assert game.board[0][0] == "X"
    assert game.current_player == "O"
    assert game.make_move(1, 1)
    assert game.board[1][1] == "O"
    assert game.current_player == "X"


def test_occupied_and_out_of_bounds_moves_are_rejected() -> None:
    game = TicTacToe()
    assert game.make_move(0, 0)

    assert not game.make_move(0, 0)
    assert not game.make_move(-1, 0)
    assert not game.make_move(3, 0)
    assert game.board[0][0] == "X"


def test_each_row_can_produce_a_winner() -> None:
    for row in range(3):
        game = TicTacToe()
        moves = [(row, 0), ((row + 1) % 3, 0), (row, 1), ((row + 1) % 3, 1), (row, 2)]

        play(game, moves)

        assert game.winner == "X"
        assert game.game_over


def test_each_column_can_produce_a_winner() -> None:
    for column in range(3):
        game = TicTacToe()
        moves = [(0, column), (0, (column + 1) % 3), (1, column), (1, (column + 1) % 3), (2, column)]

        play(game, moves)

        assert game.winner == "X"


def test_both_diagonals_can_produce_a_winner() -> None:
    main_diagonal = TicTacToe()
    play(main_diagonal, [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)])
    assert main_diagonal.winner == "X"

    other_diagonal = TicTacToe()
    play(other_diagonal, [(0, 2), (0, 0), (1, 1), (1, 0), (2, 0)])
    assert other_diagonal.winner == "X"


def test_full_board_without_winner_is_a_draw() -> None:
    game = TicTacToe()
    play(game, [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)])

    assert game.winner is None
    assert game.is_draw
    assert game.game_over
    assert not game.make_move(1, 1)


def test_reset_starts_a_clean_game() -> None:
    game = TicTacToe()
    play(game, [(0, 0), (1, 0), (0, 1)])

    game.reset()

    assert game.board == [["", "", ""], ["", "", ""], ["", "", ""]]
    assert game.current_player == "X"
    assert game.winner is None
    assert not game.is_draw
