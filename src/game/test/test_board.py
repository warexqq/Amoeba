import pytest
import numpy as np

from src.game import board


min_s = board.BoardConstants.MIN_BOARD_SIZE
max_s = board.BoardConstants.MAX_BOARD_SIZE
mid_s = int( (max_s + min_s) / 2 )


@pytest.mark.parametrize("size", [min_s, mid_s, max_s])
def test_amoeba_board_valid_size_int(size):
    test_board = board.AmoebaBoard(board_size=size)
    assert test_board.board_size == (size, size)


@pytest.mark.parametrize("size", [(min_s,), (mid_s,), (max_s,)])
def test_amoeba_board_valid_size_one_elem_tuple(size):
    test_board = board.AmoebaBoard(board_size=size)
    assert test_board.board_size == (size[0], size[0])


@pytest.mark.parametrize("size", [(min_s,min_s), (min_s,max_s), (max_s,max_s), (max_s,min_s)])
def test_amoeba_board_valid_size_double_tuple(size):
    test_board = board.AmoebaBoard(board_size=size)
    assert test_board.board_size == size


@pytest.mark.parametrize("size",
                         [min_s - 1, 0, max_s + 1, max_s * 2 ,
                          (min_s,min_s-1), (min_s,max_s+1), (max_s+1,max_s), (max_s+1,min_s-1),
                          (), (min_s,min_s,min_s)])
def test_amoeba_board_invalid_size(size):
    with pytest.raises(ValueError):
        test_board = board.AmoebaBoard(board_size=size)
        assert test_board is None


@pytest.mark.parametrize("size",['a','bad_string', '0'])
def test_amoeba_board_invalid_size_type(size):
    with pytest.raises(TypeError):
        test_board = board.AmoebaBoard(board_size=size)
        assert test_board is None


@pytest.mark.parametrize("size", [(min_s,min_s), (mid_s,max_s), (max_s,max_s), (min_s,mid_s)])
def test_amoeba_board_layout(size):
    test_board = board.AmoebaBoard(board_size=size)
    rows, cols = size
    expected_board = np.array([[board.Cell.Empty for j in range(cols)] for i in range(rows)])
    assert str(test_board) == str(expected_board)
