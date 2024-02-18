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
        print('Adding new player..')
        name = survey.routines.input('Player name: ')
        new_player = logic.player.Player(name)

        # _marks = (logic.board.Mark.X.value, logic.board.Mark.O.value)
        # mark = survey.routines.select('Select a mark: ', options= _marks)
        # new_player.cell_mark = logic.board.Mark(_marks[mark])

        self._players[name] = new_player
        print(f'New player added: {new_player}')

    def board_param_setup(self):
        self._board_size = survey.routines.numeric('Board size (at least 3 or higher): ', decimal= False)
        self._winning_length = survey.routines.numeric('Winning length size (at least 3 or higher, but not longer than the board): ', decimal= False)

        players = list(self._players.keys())

        num = survey.routines.select('Select player with mark X: ', options= players)
        playerX: logic.player.Player = self._players[players[num]]
        playerX.cell_mark = logic.board.Mark.X

        num = survey.routines.select('Select player with mark O: ', options= players)
        playerO: logic.player.Player = self._players[players[num]]
        playerO.cell_mark = logic.board.Mark.O

        self._game = logic.AmoebaGame(player_o=playerO, player_x=playerX, board_size=self._board_size, win_length=self._winning_length)


    def choose_starting_side(self):
        select_starting_player = survey.routines.inquire('Want to select the starting player? If no, random palyer is chosen. ', default=True)

        if select_starting_player:
            players = list(self._players.keys())
            player_num = survey.routines.select('Select player who starts: ', options= players)
            starting_player = self._players[players[player_num]]
            print(starting_player)
            starting_player= starting_player.cell_mark
            print(starting_player)
        else:
            starting_player = None

        self._game.choose_starting_side(starting_player)


    def play(self):
        self._game.start_game()

        while self._game.state not in [logic.State.FINISH, logic.State.ERROR]:
            player_to_move = self.game.player_x if self.game.state == logic.State.WAITING_FOR_X_TO_MOVE else self.game.player_o
            print(f"Waiting for {player_to_move} to move...")
            rows = (str(row) for row in self.game.game_board)
            row = survey.routines.select("Select row: ", options= rows)
            cols = (str(col) for col in self.game.game_board[row])
            col = survey.routines.select("Select row: ", options= cols)
            self._game.next_player_move((row,col))

        self._game.finish_game()


def main():
    term = SimpleTerminalIF()
    print("Welcome to Amoeba game's terminal version. To be able to play add at least 2 players.")
    adding_players = True
    while adding_players:
        try:
            term.add_player()
            adding_players = survey.routines.inquire('Want to add more players? ', default=True)
        except ValueError as e:
            print(e)
            continue

    if len(term._players) < 2:
        raise Exception("Not enough players..")

    term.board_param_setup()

    term.choose_starting_side()

    # term._game = logic.AmoebaGame(player_o=logic.player.Player("Bazsa",logic.board.Mark.O), player_x=logic.player.Player("Robot",logic.board.Mark.X), board_size=3, win_length=3)
    print("Let's play!")
    term.play()
