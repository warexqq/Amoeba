import pytest

from src.game import board


@pytest.mark.parametrize("size",[3, 15, 30, (3,), (20,), (30,), (3,3), (3,30), (30,30), (30,3)])
def test_amoeba_board_valid_size(size):
    test_board = board.AmoebaBoard(board_size=size)
    assert test_board.board_size == size
