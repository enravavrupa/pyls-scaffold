
# pytest is the module that provides us with testing helper functions.
# Mostly not needed initially, but you'll call on it in some cases.
# See documentation on pytest.
import pytest

# Import the module whose procedures and functions you want to test here.
import pyls
import io
import sys

# Note that the procedures below that are testing for things **must**
# have their names start with "test_" ... just as this file's name
# also starts with "test_". `pytest` will automatically pick up
# such functions and run them when you run `uvx pytest` from the
# command line.


@pytest.fixture()
def capture():
    sio = io.StringIO()
    yield sio
def test_dummy(): #by convention, for pytest fixture to work, the function names need to being with text_
    """
    A sample dummy test for illustration. This test will always succeed.
    """
    oldstdout = sys.stdout, "Two and two must be the same"
    sys.stdout = capture
    print("MEOW")
    sys.stdout = oldstdout

    capture.seek(0)
    result = capture.read()
    assert result == "MEOW\n", f"result (len = {len(result)}) = {result}, capture = {capture}"


#def test_dummy_fails():
    """
    A sample dummy test for illustration. This test will all fail.
    """
#    assert 2 == 3, "Two and three must be the same. (Really?)"
