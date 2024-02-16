import pytest

from src.game.logic import AmoebaGame, State, player, board


def test_gameplay():
    game = AmoebaGame(player_x=player.Player("1", board.Mark.X), player_o=player.Player("2", board.Mark.O))
    assert game.state == State.INIT
    game.choose_starting_side(board.Mark.X)
    assert game.state == State.READY
    game.start_game()
    assert game.state == State.WAITING_FOR_X_TO_MOVE
    game.next_player_move((0,0))
    assert game.state == State.WAITING_FOR_O_TO_MOVE
    game.next_player_move((1,0))
    assert game.state == State.WAITING_FOR_X_TO_MOVE
    game.next_player_move((0,1))
    assert game.state == State.WAITING_FOR_O_TO_MOVE
    game.next_player_move((1,1))
    assert game.state == State.WAITING_FOR_X_TO_MOVE
    game.next_player_move((0,2))
    assert game.state == State.FINISH
    assert game.winning_sequence == [(0, 0), (0, 1), (0, 2)]
