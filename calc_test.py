import pytest

from calc import sum


def test_summ():
    first = 2
    second = 1
    assert sum(first, second) == 3


def test_subtruct():
    first = 2
    second = 1
    assert sum(first, second) == 3


def test_negative():
    first = -2
    second = -1
    assert sum(first, second) == -3
