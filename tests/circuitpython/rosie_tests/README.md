# RosiePi Tests

The tests contained here in `tests/circuitpython/rosie_tests` are written for use with [RosiePi](https://github.com/physaCI/RosiePi).

# Writing Tests

RosiePi uses [pytest](https://github.com/pytest-dev/pytest/) to administer this set of tests.

## Test Filenames

pytest collects tests based on a standard filename pattern. The configuration of pytest used here is set to only recognize filenames that follow this pattern: `test_*.py`. Other filename patterns will not be collected (e.g `*_test.py`).

## Plugin Usage

A pytest plugin (`pytest_rosie`) is included with RosiePi that allows tests to utilize the test controller, as well as board-interaction methods via `tools/cpboard.py`. All other standard pytest plugins are available; `capsys` is especially helpful during test development to inspect values via `print`.

The board interaction methods in the plugin can be used by placing the appropriate parameter(s) in a test function's signature:

```python
def test_board_interaction(board_name, board):
```

##### board_name
`board_name` is a string that denotes the current board being tested (e.g. `'itsybitsy_m4_express'`). It is useful when wanting to tailor or skip a test, based on the board:

```python
def test_board_interaction(board_name):
    if board_name in ['itsybitsy_m4_express']:
        pytest.skip()
```

##### board
`board` is the `tools/cpboard.py::CPBoard` object created when the RosiePi test controller connects to the board being tested. All available functions from that object are accessible. A context manager is available, and should be used. Also, the REPL on the board is reset for each test function, to provide a "clean slate" for each test. The two main methods to use will be `exec()` and `eval()`:

```python
def test_board_interaction(board):
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
```

- `CPboard` REPL interaction uses the "raw REPL". The raw REPL is designed for machine-to-machine use, and does not echo or print executions. The raw REPL also returns all representations as `bytes`, versus `string` (see `eval` below).

- The `exec` method is used to execute a command, without the expectation of an implicitly returned result. Exceptions will be returned, however. If you wish to reset the REPL within a context managed instance or test function, pass the keyword argument `reset_repl=True`: `exec("foo.deinit()", reset_repl=True)`.

- The `eval` method is used to encapsulate a command inside a `print` call, retrieve the returned result, and transform the raw REPL's bytes result into its CPython representation. Example:
```python
foo = board.eval("[1, 2, 3]") ->
# transformed to `print("[1, 2, 3]")` ->
# `print("[1, 2, 3]") is executed on the board ->`
# printed result is `b"[1, 2, 3]"` on the board ->
# result is retrieved and further eval'd into `foo = [1, 2, 3]`
# `foo` now equals `[1, 2, 3]` in the pytest script
```

#### Running Tests During Development
The easiest way to run tests that your are writing, is to install RosiePi and either using the pytest plugin locally or running RosiePi with it's `rosiepi` console script.
