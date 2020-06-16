import pytest

def test_import(board):
    """ Verify import successfully occurs.
    """
    with board:
        result = board.exec("from digitalio import DigitalInOut")

        assert "importerror" not in result.decode().lower()

def test_available_members(board):
    """ Verify the attributes and members available in
        ``digitalio.DigitalInOut``.

        Expected result: ['__class__', '__name__', 'DigitalInOut', 'Direction',
                          'DriveMode', 'Pull']
    """

    expected = {'__class__', '__enter__', '__exit__', '__name__', 'deinit',
                'direction', 'drive_mode', 'pull', 'switch_to_input',
                'switch_to_output', 'value'}

    with board:
        board.debug = True

        board.exec("from digitalio import DigitalInOut")

        result = board.eval("dir(DigitalInOut)")

        final_result = set(result)

        assert not final_result.difference(expected)

def test_pins_initial_state(board, capsys):
    """ Verify initial states of pins with DigitalInOut as input.
    """
    imports = [
        "import board",
        "import digitalio"
    ]
    with board:
        for stmt in imports:
            board.exec(stmt)

        pins = board.eval("dir(board)")
        pins = [pin for pin in pins if pin.startswith("D")]

        for pin in pins:
            board.exec(f"pin_{pin} = digitalio.DigitalInOut(board.{pin})")
            pin_direction = board.eval(
                f"pin_{pin}.direction == digitalio.Direction.INPUT"
            )

            assert pin_direction
