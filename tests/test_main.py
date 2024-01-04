# Run make check-codestyle command to check the codestyle
from uacp import main
import pytest


def test_add_numbers():
    assert main.add_numbers(1, 2) == 3
    assert main.add_numbers(-1, -2) == -3
    assert main.add_numbers(0, 0) == 0
    assert main.add_numbers(1.5, 2.5) == 4.0
    assert main.add_numbers(-1.5, -2.5) == -4.0
