import pytest

from src.game.player import Player, board


def test_simple_player_o():
    new_player = Player('test_name', board.Mark.O)
    assert new_player.name == 'test_name'
    assert new_player.cell_mark != 'o'
    assert new_player.cell_mark == board.Mark.O


def test_simple_player_x():
    new_player = Player('test_name', board.Mark.X)
    assert new_player.name == 'test_name'
    assert new_player.cell_mark != 'x'
    assert new_player.cell_mark == board.Mark.X


@pytest.mark.parametrize("wrong_mark", ['X','x','o','O','0'])
def test_player_wrong_mark(wrong_mark):
    with pytest.raises(TypeError):
        new_player = Player('test_name', wrong_mark)
