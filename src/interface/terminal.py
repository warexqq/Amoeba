import survey

from src.game import logic

class SimpleTerminalIF:
    def __init__(self) -> None:
        self._game = None
        self._players = {}

    @property
    def game(self):
        return self._game

    def add_player(self):
        print('Adding new player!')
        name = survey.routines.input('Player name: ')
        _marks = (logic.board.Cell.X, logic.board.Cell.O)
        mark = survey.routines.select('Select a mark: ', options= _marks)
        new_player = logic.player.Player(name, mark)
        self._players[name] = new_player
        print(f'New player added: {new_player}')


    def play(self):
        pass



if __name__ == "__main__":
    term = SimpleTerminalIF()
    term.add_player()
