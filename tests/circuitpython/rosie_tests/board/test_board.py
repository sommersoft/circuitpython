def test_import(board):
    """ Verify import successfully occurs.
    """
    with board:
        result = board.exec("import board")

        assert "importerror" not in result.decode().lower()

def test_available_members(board_name, board):
    """ Verify the attributes and members available in
        ``board``.

        Expected result: board dependent. See ``expected`` variable in source code.
    """

    expected = {
        'itsybitsy_m4_express': {'__class__', 'A0', 'A1', 'A2', 'A3',
                                 'A4', 'A5', 'APA102_MOSI', 'APA102_SCK',
                                 'D0', 'D1', 'D10', 'D11', 'D12', 'D13',
                                 'D2', 'D3', 'D4', 'D5', 'D7', 'D9',
                                 'I2C', 'MISO', 'MOSI', 'RX', 'SCK',
                                 'SCL', 'SDA', 'SPI', 'TX', 'UART'},

        'metro_m4_express': {'__class__', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5',
                             'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D2',
                             'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'I2C',
                             'LED_RX', 'LED_TX', 'MISO', 'MOSI', 'NEOPIXEL',
                             'RX', 'SCK', 'SCL', 'SDA', 'SPI', 'TX', 'UART'},
    }

    with board:
        board.debug = True

        board.exec("import board")

        result = board.eval("dir(board)")

        final_result = set(result)

        assert not final_result.difference(expected[board_name])
