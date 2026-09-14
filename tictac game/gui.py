"""Tkinter interface for the Tic-Tac-Toe game."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from logic import TicTacToe
except ImportError:  # Support importing as tictac game's package-like module.
    from .logic import TicTacToe


class TicTacToeApp:
    """Display and control a two-player Tic-Tac-Toe game."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.game = TicTacToe()
        self.status = tk.StringVar()
        self.buttons: list[list[ttk.Button]] = []
        self._build_interface()
        self._refresh()

    def _build_interface(self) -> None:
        container = ttk.Frame(self.root, padding=20)
        container.grid(row=0, column=0)

        ttk.Label(container, text="Tic-Tac-Toe", font=("TkDefaultFont", 20, "bold")).grid(
            row=0, column=0, columnspan=3, pady=(0, 6)
        )
        ttk.Label(container, textvariable=self.status, font=("TkDefaultFont", 11)).grid(
            row=1, column=0, columnspan=3, pady=(0, 14)
        )

        board = ttk.Frame(container)
        board.grid(row=2, column=0, columnspan=3)
        for row in range(self.game.SIZE):
            button_row: list[ttk.Button] = []
            for column in range(self.game.SIZE):
                button = ttk.Button(
                    board,
                    text="",
                    command=lambda r=row, c=column: self._play(r, c),
                    width=5,
                )
                button.grid(row=row, column=column, padx=3, pady=3, ipady=12)
                button_row.append(button)
            self.buttons.append(button_row)

        ttk.Button(container, text="New Game", command=self._new_game).grid(
            row=3, column=0, columnspan=3, pady=(16, 0)
        )

    def _play(self, row: int, column: int) -> None:
        if self.game.make_move(row, column):
            self._refresh()

    def _new_game(self) -> None:
        self.game.reset()
        self._refresh()

    def _refresh(self) -> None:
        for row in range(self.game.SIZE):
            for column in range(self.game.SIZE):
                mark = self.game.board[row][column]
                self.buttons[row][column].configure(text=mark)
                state = "disabled" if mark or self.game.game_over else "normal"
                self.buttons[row][column].configure(state=state)

        if self.game.winner:
            self.status.set(f"Player {self.game.winner} wins!")
        elif self.game.is_draw:
            self.status.set("It's a draw!")
        else:
            self.status.set(f"Player {self.game.current_player}'s turn")


def run() -> None:
    """Create the window and start Tkinter's event loop."""
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()
