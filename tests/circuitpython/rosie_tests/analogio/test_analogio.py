import pytest

def test_import(board):
    """ Verify import successfully occurs.
    """
    with board:
        result = board.exec("import analogio")

        assert "importerror" not in result.decode().lower()
