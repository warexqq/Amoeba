import random
from enum import Enum, auto

from . import board, player


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


# Improvement study: try implementing it with statemachine pip module
class AmoebaGame:

    def __init__(self, player_x: player.Player, player_o: player.Player, board_size = 3, win_length = 3) -> None:
        if player_x.cell_mark != board.Cell.X or player_o.cell_mark != board.Cell.O:
            raise TypeError(f"player_x and player_o shall have the required cell marks.")
        self._player_x = player_x
        self._player_o = player_o
        self._starting_side = None
        self._board = board.AmoebaBoard(board_size)
        if win_length < board.BoardConstants.MIN_BOARD_SIZE or win_length > board_size:
            raise ValueError(f"win_length invalid size. Most be between {board.BoardConstants.MIN_BOARD_SIZE} and your chosen board_size ({board_size}).")
        self._win_length = win_length
        self._state = State.INIT

    @property
    def player_x(self):
        return self._player_x

    @property
    def player_o(self):
        return self._player_o

    @property
    def game_board(self):
        return self._board

    @property
    def win_length(self):
        return self._win_length

    @property
    def state(self):
        return self._state

    def choose_starting_side(self, starting_side) -> None:
        """ Using player's decision, if its not X or O random side will be chosen."""
        if self.state != State.INIT:
            raise State.IncorrectStateException()

        if starting_side == board.Cell.X or starting_side == board.Cell.O:
            self._starting_side = starting_side
        else:
            self._starting_side = random.choice([board.Cell.X, board.Cell.O])

        self._state = State.READY

    def start_game(self):
        if self.state not in (State.INIT, State.READY):
            raise State.IncorrectStateException()

        if not self._starting_side:
            self.choose_starting_side("pick random")

        if self._starting_side == board.Cell.X:
            self._state = State.WAITING_FOR_X_TO_MOVE
        elif self._starting_side == board.Cell.O:
            self._state = State.WAITING_FOR_O_TO_MOVE
        else:
            self._state = State.ERROR
            raise ValueError("Starting side shall be either X or O")

    def next_player_move(self, place):
        if self.state == State.WAITING_FOR_X_TO_MOVE:
            self.game_board.update_cell(place, board.Cell.X)
            seq = self.find_winning_sequence(player_mark=self.player_x.cell_mark, last_move=place)
            if seq:
                self._state = State.FINISH
            else:
                self._state = State.WAITING_FOR_O_TO_MOVE
        elif self.state == State.WAITING_FOR_O_TO_MOVE:
            self.game_board.update_cell(place, board.Cell.O)
            seq = self.find_winning_sequence(player_mark=self.player_x.cell_mark, last_move=place)
            if seq:
                self._state = State.FINISH
            else:
                self._state = State.WAITING_FOR_X_TO_MOVE
        else:
            raise State.IncorrectStateException()

    def find_winning_sequence(self, player_mark: board.Cell, last_move: tuple[int, int]) -> list:
        # Function to find the winning sequence of marks for a specific player
        class Direction:
            HORIZONTAL    = (0, 1)
            VERTICAL      = (1, 0)
            MAIN_DIAGONAL = (1, 1)                  # Diagonal (top-left to bottom-right)
            ANTI_DIAGONAL = (-1, 1)                 # Reverse diagonal (bottom-left to top-right)

        def in_range(i, j):
            return 0 <= i < self.game_board.board.shape[0] and 0 <= j < self.game_board.board.shape[1]

        def get_sequence(dir: Direction):
            row, col = last_move
            drow, dcol = dir
            sequence = [last_move]
            for elem in range(1, self.win_length):          # Iterate up towards Direction
                new_row, new_col = row + elem * drow, col + elem * dcol
                if in_range(new_row, new_col) and self.game_board.board[new_row, new_col] == player_mark.value:
                    sequence.append((new_row, new_col))
                else:
                    break
            for elem in range(1, self.win_length):          # Iterate backwards from last move
                new_row, new_col = row - elem * drow, col - elem * dcol
                if in_range(new_row, new_col) and self.game_board.board[new_row, new_col] == player_mark.value:
                    sequence.insert(0,(new_row, new_col))
                else:
                    break
            return sequence


        sequence = get_sequence(Direction.HORIZONTAL)
        print(sequence)
        if len(sequence) >= self.win_length:
            return sequence

        sequence = get_sequence(Direction.VERTICAL)
        print(sequence)
        if len(sequence) >= self.win_length:
            return sequence

        sequence = get_sequence(Direction.MAIN_DIAGONAL)
        print(sequence)
        if len(sequence) >= self.win_length:
            return sequence

        sequence = get_sequence(Direction.ANTI_DIAGONAL)
        print(sequence)
        if len(sequence) >= self.win_length:
            return sequence

        return []

    def finish_game(self):
        pass
