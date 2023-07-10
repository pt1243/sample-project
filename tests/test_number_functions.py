import pytest
import numpy as np
from my_package.number_functions import add_one, subtract_one, sum_array


@pytest.mark.parametrize("test_input,expected", [
    (1, 2),
    (0, 1),
    (-4, -3),
    (2.5, 3.5),
])
def test_add_one(test_input, expected):
    assert add_one(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (1, 0),
    (0, -1),
    (-4, -5),
    (2.5, 1.5),
])
def test_subtract_one(test_input, expected):
    assert subtract_one(test_input) == expected


def test_add_one_typeerror():
    with pytest.raises(TypeError):
        add_one('some string')


def test_subtract_one_typeerror():
    with pytest.raises(TypeError):
        subtract_one('another string')


@pytest.mark.parametrize("test_input,expected", [
    (np.array([1, 2]), 3),
    (np.array([]), 0),
    (np.ones(3), 3),
    (np.zeros(5), 0),
])
def test_sum_array(test_input, expected):
    assert sum_array(test_input) == expected
