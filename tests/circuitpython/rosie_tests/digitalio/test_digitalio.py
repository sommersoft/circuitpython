import pytest

def test_import(board):
    """ Verify import successfully occurs.
    """
    with board:
        result = board.exec("import digitalio")

        assert "importerror" not in result.decode().lower()

def test_available_members(board):
    """ Verify the attributes and members available in ``digitalio``.

        Expected result: ['__class__', '__name__', 'DigitalInOut', 'Direction',
                          'DriveMode', 'Pull']
    """

    expected = {'__class__', '__name__', 'DigitalInOut', 'Direction',
                'DriveMode', 'Pull'}

    with board:
        board.exec("import digitalio")

        result = board.eval("dir(digitalio)")

        final_result = set(result)

        assert not final_result.difference(expected)
