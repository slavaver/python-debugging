import pytest

from task3 import add_matrices

def test_add_matrices():
    matrix1 = [[1, 2, 3], [4, 5, 6], [1, 8, 9]]
    matrix2 = [[1, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected_result = [[2, 10, 10], [10, 10, 10], [4, 10, 10]]
    result = add_matrices(matrix1, matrix2)
    assert result == expected_result

def test_add_matrices_with_different_dimensions():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    with pytest.raises(ValueError):
        add_matrices(matrix1, matrix2)

def test_add_matrices_with_negative_numbers():
    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[-9, 8, -7], [6, -5, 4], [-3, 2, -1]]
    expected_result = [[-8, 6, -4], [2, 0, -2], [4, -6, 8]]
    result = add_matrices(matrix1, matrix2)
    assert result == expected_result