from src.game import board


class Player:
    def __init__(self, name, cell_mark: board.Mark = board.Mark.Empty) -> None:
        self.name = name
        self.cell_mark = cell_mark

    def __str__(self) -> str:
        return f"<Player> {self.name} : {self.cell_mark}"

    def __repr__(self) -> str:
        return f"<Player> {self.name} : {self.cell_mark}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
        else:
            raise ValueError('Name shall be at least 1 charcter long string')

    @property
    def cell_mark(self):
        return self._cell_mark

    @cell_mark.setter
    def cell_mark(self, value: board.Mark):
        if not isinstance(value, board.Mark):
            raise TypeError(f"Cell must have type {board.Mark}")
        self._cell_mark = value
