from calculator import add, subtract, multiply, divide, matrix_multiplication
import pytest

def test_add_success():
    x = 5
    y = 234


    result = add(x, y)

    assert result == 239

def test_subtract_success():
    x = 5
    y = 234


    result = subtract(x, y)

    assert result == -229


def test_multiply_success():
    x = 5
    y = 234


    result = multiply(x, y)

    assert result == 234 * 5

def test_divide_success():
    x = 5
    y = 234


    result = divide(x, y)

    assert result == 5 / 234