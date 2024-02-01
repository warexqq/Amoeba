from enum import Enum


class CellValue(Enum):
    X = 'x'
    O = 'o'


class BoardCell:
    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> CellValue:
        return self._value

    @value.setter
    def value(self, new_val: CellValue) -> None:
        if new_val in CellValue:
            self._value = new_val

    def __repr__(self) -> str:
        return f"<BoardCell value: '{self._value}'>"

    def __str__(self) -> str:
        return str(self._value)

    def __eq__(self, other):
        if not isinstance(other, BoardCell):
            return NotImplemented
        return self.value == other.value


class BoardConstants:
    @property
    def MIN_BOARD_SIZE(self):
        return 3

    @property
    def MAX_BOARD_SIZE(self):
        return 30

board_constants = BoardConstants()


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
            if not board_constants.MIN_BOARD_SIZE <= board_size_number <= board_constants.MAX_BOARD_SIZE:
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

        rows, cols = self._board_size
        self._board = [[BoardCell() for j in range(cols)] for i in range(rows)]

    @property
    def board_size(self):
        return self._board_size

    @property
    def board(self):
        return self._board


if __name__ == "__main__":
    my_board = AmoebaBoard(3)
    print(my_board.board)
    print(my_board.board[0][0])