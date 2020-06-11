# RosiePi Test Script for digitalio
import pytest

SKIP = [
    'itsybitsy_m4_express',
]


def test_digitalio_import(board, capsys):
    with board:
        result = board.exec("import digitali")

        assert "importerror" not in result.decode().lower()

def test_digitalio_import_fail(board_name, board, capsys):
    if board_name in SKIP:
        pytest.skip()

    with board:
        result = board.exec("import digital")

        print(result)

        assert "importerror" not in result.decode().lower()

def test_direction_available_members(board, capsys):

    with board:
        board.debug = True

        result = board.exec("import digitalio")

        result = board.exec("print(dir(digitalio.Direction))")

        assert result.decode().strip("\r\n") == str(['__class__', '__name__', 'INPUT', 'OUTPUT'])
        #board.exec("print(dir(digitalio.Direction))")
