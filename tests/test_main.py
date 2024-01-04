import pytest
from uacp import main


def test_add_numbers():
    assert main.add_numbers(1, 2) == 3
    assert main.add_numbers(-1, -2) == -3
    assert main.add_numbers(0, 0) == 0
    assert main.add_numbers(1.5, 2.5) == 4.0
    assert main.add_numbers(-1.5, -2.5) == -4.0
