import numpy as np
from enum import Enum


class Mark(Enum):
    X = 'x'
    O = 'o'
    Empty = None

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class BoardConstants:
    MIN_BOARD_SIZE = 3
    MAX_BOARD_SIZE = 30


class AmoebaBoard:
    """
    Class used to represent an amoebe board.
    A board is a two dimensional matrix, whose sides can be the same or differ.
    """

    def __init__(self, board_size) -> None:
        """
        Parameters
        ----------
        board_size: int or tuple of ints
            yields the shape of the 2D board
        """
        self._board_size = None

        def valid_num_board_size(board_size_number: int) -> bool:
            if not isinstance(board_size_number, int):
                raise TypeError(f"Input shall be an integer, but '{type(board_size_number)}' was given.")
            if not BoardConstants.MIN_BOARD_SIZE <= board_size_number <= BoardConstants.MAX_BOARD_SIZE:
                raise ValueError(f"'{board_size_number}' is not a valid number.")
            return True

        if isinstance(board_size, int):
            if valid_num_board_size(board_size):
                self._board_size = (board_size, board_size)
        elif isinstance(board_size, tuple):
            if len(board_size) == 1:
                board_size = board_size[0]
                if valid_num_board_size(board_size):
                    self._board_size = (board_size, board_size)
            elif len(board_size) == 2:
                if valid_num_board_size(board_size[0]) and valid_num_board_size(board_size[1]):
                    self._board_size = board_size
            else:
                raise ValueError(f"Invalid size of tuple. Len can be 1 or 2, but {len(board_size)} was given.")
        else:
            raise TypeError(f"Input must be integer or tuple, '{type(board_size)}' was given.")

        self._board = None
        self._clear_board()

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self) -> str:
        return str(self.board)

    @property
    def board_size(self):
        return self._board_size

    @property
    def board(self):
        return self._board

    def _clear_board(self):
        rows, cols = self._board_size
        self._board = np.array([[Mark.Empty for j in range(cols)] for i in range(rows)], dtype=Mark)

    def update_cell(self, place: tuple, cell_mark: Mark):
        if not isinstance(place, tuple) and len(tuple) != 2:
            raise ValueError("A place has to be a 2 elem tuple, with the coordinates of the mark")
        if not isinstance(cell_mark, Mark):
            raise TypeError("A mark has to be Mark type")

        x, y = place
        self._board[x][y] = cell_mark



if __name__ == "__main__":
    my_board = AmoebaBoard(3)
    print(my_board.board.dtype)
    print(my_board)
    print(my_board[0])
    print(my_board[0][0])

    my_board[0][0] = Mark.X

    print(my_board)
    print(my_board[0][0])
