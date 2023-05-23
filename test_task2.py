import pytest

from task1 import calculate

def test_calculate_subtraction():
    result = calculate(6, "-", 1.5)
    assert result == 4.5

def test_calculate_multiplication():
    result = calculate(-4, "*", 8)
    assert result == -32

def test_calculate_division():
    result = calculate(49, "/", -7)
    assert result == -7

def test_calculate_invalid_operation():
    result = calculate(8, "m", 2)
    assert result is None

def test_calculate_division_by_zero():
    result = calculate(4, "/", 0)
    assert result is None
