import board


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
    def __init__(self, player1: Player, player2: Player, board_size = 3) -> None:
        if not isinstance(player1, Player) or not isinstance(player2, Player):
            raise TypeError(f"player1 and player2 shall be instances of {Player}")
        self._player1 = player1
        self._player2 = player2
        self._board = board.AmoebaBoard(board_size)

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player1

    @property
    def board(self):
        return self._board



if __name__ == "__main__":
    print(AmoebaGame(Player("1", board.Cell.X),Player("2", board.Cell.O)))