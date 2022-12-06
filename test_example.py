from example import *


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(1000000000000000000, 2) == 1000000000000000002


def test_multiply():
    assert multiply(2, 1) == 2
    assert multiply(10, 5) == 50


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5


def test_divide():
    assert divide(0, 142) == 0
    assert divide(10, 2) == 5


def test_mod():
    assert mod(5, 3) == 2
    assert mod(4, 2) == 0
