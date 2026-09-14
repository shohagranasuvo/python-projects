"""Launch the Tic-Tac-Toe desktop application."""

try:
    from gui import run
except ImportError:  # Support importing as tictac game's package-like module.
    from .gui import run


if __name__ == "__main__":
    run()
