import pytest
from uacp import UACP


def test_foo():
    assert UACP.foo(1) == True

def test_bar():
    assert UACP.bar("test") == "expected_result"

def test_baz():
    assert UACP.baz([1, 2, 3]) == [3, 2, 1]
