import random
from enum import Enum, auto

from src.game import board


class Player:
    def __init__(self, name, cell_mark: board.Cell) -> None:
        self._name = name
        self._cell_mark = cell_mark

    @property
    def name(self):
        return self._name

    @property
    def cell_mark(self):
        return self._cell_mark

    @cell_mark.setter
    def cell_mark(self, value: board.Cell):
        if not isinstance(value, board.Cell):
            raise TypeError(f"Cell must have type {board.Cell}")
        self._cell_mark = value


class AmoebaGame:
    class State(Enum):
        INIT = auto()
        READY = auto()
        WAITING_FOR_X_TO_MOVE = auto()
        WAITING_FOR_O_TO_MOVE = auto()
        FINISH = auto()
        ERROR = auto()

    class IncorrectStateException(Exception):
        """Custom exception for handling incorrect states in the game's internal state machine."""
        def __init__(self, message="Function called in incorrect state"):
            self.message = message
            super().__init__(self.message)

    def __init__(self, player_x: Player, player_o: Player, board_size = 3, row_size = 3) -> None:
        if not player_x.cell_mark == board.Cell.X or player_o.cell_mark == board.Cell.O:
            raise TypeError(f"player_x and player_o shall have the required cell marks.")
        self._player_x = player_x
        self._player_o = player_o
        self._board = board.AmoebaBoard(board_size)
        if row_size < board.board_constants.MIN_BOARD_SIZE or row_size > board_size:
            raise ValueError(f"row_size invalid size. Most be between {board.board_constants.MIN_BOARD_SIZE} and your chosen board_size ({board_size}).")
        self._row_size = row_size
        self._state = self.State.INIT
        self._starting_side = None

    @property
    def player_x(self):
        return self._player_x

    @property
    def player_o(self):
        return self._player_o

    @property
    def game_board(self):
        return self._board

    def _check_row_complete(self):
        pass

    def choose_starting_side(self, starting_side) -> None:
        """ Using player's decision, if its not X or O random side will be chosen."""
        if self._state != self.State.INIT:
            raise self.IncorrectStateException()

        if starting_side == board.Cell.X or starting_side == board.Cell.O:
            self._starting_side = starting_side
        else:
            self._starting_side = random.choice([board.Cell.X, board.Cell.O])

        self._state = self.State.READY

    def start_game(self):
        if self._state not in (self.State.INIT, self.State.READY):
            raise self.IncorrectStateException()

        if not self._starting_side:
            self.choose_starting_side("pick random")

        if self._starting_side == board.Cell.X:
            self._state = self.State.WAITING_FOR_X_TO_MOVE
        elif self._starting_side == board.Cell.O:
            self._state = self.State.WAITING_FOR_O_TO_MOVE
        else:
            self._state = self.State.ERROR
            raise ValueError("Starting side shall be either X or O")

    def next_player_move(self, place):
        if self._state == self.State.WAITING_FOR_X_TO_MOVE:
            self.game_board.update_cell(place, board.Cell.X)
        elif self._state == self.State.WAITING_FOR_O_TO_MOVE:
            self.game_board.update_cell(place, board.Cell.O)
        else:
            raise self.IncorrectStateException()

        self._check_row_complete()

    def finish_game(self):
        pass



if __name__ == "__main__":
    print(AmoebaGame(Player("1", board.Cell.X),Player("2", board.Cell.O)))