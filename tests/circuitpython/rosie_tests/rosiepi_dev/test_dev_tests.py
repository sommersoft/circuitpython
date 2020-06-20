import pytest

def test_pytest_skip_board(board_name, board, capsys):
    """ DEV: only used to test skipping by board_name
    """
    if board_name in ["metro_m4_express"]:
        pytest.skip()

    with board:
        result = board.exec("import bord")

        print(result)

        assert "importerror" not in result.decode().lower()
