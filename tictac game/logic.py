"""Core rules for a two-player game of Tic-Tac-Toe."""

from __future__ import annotations

from typing import Optional


class TicTacToe:
    """Manage a 3x3 Tic-Tac-Toe board without any user-interface code."""

    SIZE = 3
    EMPTY = ""
    PLAYERS = ("X", "O")

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Start a fresh game with X taking the first turn."""
        self.board = [[self.EMPTY for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.current_player = self.PLAYERS[0]
        self.winner: Optional[str] = None
        self.is_draw = False

    @property
    def game_over(self) -> bool:
        """Return whether the game has ended."""
        return self.winner is not None or self.is_draw

    def make_move(self, row: int, column: int) -> bool:
        """Place the current player's mark and return whether it was accepted."""
        if self.game_over or not self._is_valid_position(row, column):
            return False
        if self.board[row][column] != self.EMPTY:
            return False

        player = self.current_player
        self.board[row][column] = player
        if self._has_won(player):
            self.winner = player
        elif all(cell != self.EMPTY for line in self.board for cell in line):
            self.is_draw = True
        else:
            self.current_player = self.PLAYERS[1] if player == self.PLAYERS[0] else self.PLAYERS[0]
        return True

    def _is_valid_position(self, row: int, column: int) -> bool:
        return 0 <= row < self.SIZE and 0 <= column < self.SIZE

    def _has_won(self, player: str) -> bool:
        lines = self.board + [
            [self.board[row][column] for row in range(self.SIZE)]
            for column in range(self.SIZE)
        ]
        lines.extend(
            [
                [self.board[index][index] for index in range(self.SIZE)],
                [self.board[index][self.SIZE - 1 - index] for index in range(self.SIZE)],
            ]
        )
        return any(all(cell == player for cell in line) for line in lines)
