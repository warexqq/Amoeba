from src.game import board


class Player:
    def __init__(self, name, cell_mark: board.Cell) -> None:
        self._name = name
        self.cell_mark = cell_mark

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
