import pytest

from task1 import find_minimum

def test_find_minimum_with_positive_numbers():
    numbers = [5, 3, 8, 2, 9]
    assert find_minimum(numbers) == 2

def test_find_minimum_with_negative_numbers():
    numbers = [-10, -5, -8, -2, -9]
    assert find_minimum(numbers) == -10

def test_find_minimum_with_mixed_numbers():
    numbers = [10, -5, 3, -2, 7]
    assert find_minimum(numbers) == -5

def test_find_minimum_with_single_number():
    numbers = [7]
    assert find_minimum(numbers) == 7

def test_find_minimum_with_empty_list():
    numbers = []
    assert find_minimum(numbers) is None
